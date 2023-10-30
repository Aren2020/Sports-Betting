from rest_framework.views import APIView
from rest_framework.response import Response
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

            output = {'status': 'Ok'}
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
