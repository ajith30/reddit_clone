from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    #path('login/', views.loginView, name='login'),
    #path('logout/', views.logoutView, name='logout'),
]
