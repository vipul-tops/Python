from django.contrib import admin
from django.urls import path
from myapp.views import BookList,BookDetail
# Register your models here.

urlpatterns = [
    path('',BookList.as_view()),
    path('api/books/<int:pk>/',BookDetail.as_view()),
    path('admin/', admin.site.urls),
]