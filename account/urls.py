from django.urls import path
from django.urls.resolvers import URLPattern
from account import views

urlpatterns = [
    #회원가입!
    path('signup/', views.signup, name='signup'),
    #로그인
    path('login/', views.login, name='login'),
    #로그아웃
    path('logout/', views.logout, name='logout'),
]