from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import VerifyUser
from .mailsender import codeGenerator,send_mail

class RegistrationView(APIView):
    def post(self,request):
        data = request.data
        
        if data['status'] == 'Verified':
            user = User.objects.create(username = data['username'])
            user.set_password(data['password'])
            user.save()

            VerifyUser.objects.create(user = user,
                                      email = data['email'])

            output = {'status': 'ok'}
            return Response(output)
        else:
            if User.objects.filter(username = data['username']).exists():
                return Response({'status':'UserAlreadyExit'})
            
            # Sending mail
            code = codeGenerator()
            to = data['email']
            send_mail(to,code)

            output = {'code': code}
            return Response(output)

class CustomAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data, context = {'request': request})
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        verifyuser = VerifyUser.objects.get(user = user)
        token, created = Token.objects.get_or_create(user = user)

        base_url = request.build_absolute_uri('/')[:-1]
        image_url = base_url + '/media' + verifyuser.profile_picture.url.rsplit('media')[-1]
        response_data = {
            'token': token.key,
            'profile_picture_url': image_url,
        }
        return Response(response_data, status=status.HTTP_200_OK)

class EditView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        verifyuser = VerifyUser.objects.get(user = request.user)
        profile_picture = request.FILES.get('profile_picture')
        username = request.POST.get('username')
        
        if User.objects.filter(username = username).exclude(username = request.user.username).exists():
            return Response({'response': 'UserAlreadyExists'})
        elif not username:
            return Response({'response': 'NoUserName'})
        else:
            request.user.username = username
            request.user.save()
            
        if profile_picture:
            verifyuser.profile_picture = request.FILES.get('profile_picture')
            verifyuser.save()

        return Response({'status':'ok'})