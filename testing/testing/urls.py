"""testing URL Configuration

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
from deep import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('monthly/',views.Monthly,name='monthly'),
    path('mobilem/',views.mobilem,name='mobilem'),
    path('mobiley/',views.mobiley,name='mobiley'),
    path('basicm/',views.basicm,name='basicm'),
    path('basicy/',views.basicy,name='basicy'),
    path('standardm/',views.standardm,name='standardm'),
    path('standardy/',views.standardy,name='standardy'),
    path('premiumm/',views.premiumm,name='premiumm'),
    path('premiumy/',views.premiumy,name='premiumy'),
    path('yearly/',views.Yearly,name='yearly'),
    path('checkout/',views.checkout,name='checkout'),
    path('logout/',views.LogoutPage,name='logout'),
    path('success/',views.success,name='success'),
    path('cancel/',views.cancel,name='cancel'),
]
