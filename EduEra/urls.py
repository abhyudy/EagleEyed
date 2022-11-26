from django.contrib import admin
from django.urls import path,include
from EduEra import views

urlpatterns = [
    path('',views.index,name="home"),
    path('studentform',views.studentform,name='studentform'),
    path('teacherform',views.teacherform,name='teacherform'),
    path('signinuser',views.signinuser,name='signinuser'),
    path('signout',views.signout,name='signout'),
    path('lobby', views.lobby),
    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]
