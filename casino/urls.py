from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('account/', include('log.urls')),
    path('sport/', include('sport.urls')),
    path('admin/', admin.site.urls),
]
