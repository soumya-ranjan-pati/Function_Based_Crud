from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('save/',views.save,name='save'),
    path('details/',views.details,name='details'),
    path('update/',views.update,name='update'),
    path('update_data/',views.update_data,name='update_data'),
    path('delete/',views.delete,name='delete'),
    path('login/',views.login,name='login'),
    path('login_page/',views.login_page,name='login_page'),
]