
from django.urls import path
from . import views

urlpatterns = [
    path('',views.test,name='test'),
    path('add-emp/',views.add_emp,name='add-emp'),
    ]
