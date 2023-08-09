
from django.urls import path
from . import views

urlpatterns = [
    path('',views.test,name='test'),
    path('add-employee/',views.add_employee,name='add-employee'),
]
