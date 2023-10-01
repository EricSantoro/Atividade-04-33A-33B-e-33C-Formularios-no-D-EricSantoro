"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app_eric import views
urlpatterns = [ path('',views.home, name='remnant'),
    path('admin/', admin.site.urls),
    path('motivos',views.create_motivos),   
    path('motivos/update/<id>',views.update_motivos),
    path('motivos/delete/<id>',views.delete_motivos),
    path('sensações',views.create_sensações),   
    path('sensações/update/<id>',views.update_sensações),
    path('sensações/delete/<id>',views.delete_sensações)
   
    
]
