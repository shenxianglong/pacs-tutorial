"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from server import  views  as server_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('read0/',server_views.read0),
    path('read1/',server_views.read1),
    path('read2/', server_views.read2),
    path('read3/', server_views.read3),
    path('read4/', server_views.read4),
    path('read5/', server_views.read5),
    path('read6/', server_views.read6),
    path('read7/', server_views.read7),
    path('read8/', server_views.read8),
    path('read9/', server_views.read9),

]
