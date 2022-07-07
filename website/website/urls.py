"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login.views import callLogin
from registro.views import callRegister
from index.views import indexCall
from asistencia.views import asistenciaCall
from configuracion.views import configuracionCall
from asistenciaFicha.views import asistenciaFichaCall

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', callLogin),
    path('registro/',callRegister),
    path('index/',indexCall),
    path('asistencia/',asistenciaCall),
    path('configuracion/',configuracionCall),
    path('asistenciaFicha/',asistenciaFichaCall)
]
