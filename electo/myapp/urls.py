from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('seller-index/',views.seller_index,name='seller-index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('edit-profile/',views.edit_profile,name='edit-profile'),

    #seller
    path('seller-add-product/',views.seller_add_product,name='seller-add-product'),
    path('seller-view-product/',views.seller_view_product,name='seller-view-product'),
    path('ajax/validate_email/',views.validate_email,name='validate_email'),
    path('ajax/validate_oldpassword/',views.validate_oldpassword,name='validate_oldpassword'),
    path('ajax/validate_newpassword/',views.validate_newpassword,name='validate_newpassword'),
]