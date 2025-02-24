from django.contrib import admin
from django.urls import path
from User import views

urlpatterns = [
    path('adminn/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),

]
