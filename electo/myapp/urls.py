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
    path('shop/',views.shop,name='shop'),

    #seller
    path('seller-add-product/',views.seller_add_product,name='seller-add-product'),
    path('seller-view-product/',views.seller_view_product,name='seller-view-product'),
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
    path('seller-edit-product/<int:pk>/',views.seller_edit_product,name='seller-edit-product'),
    path('seller-delete-product/<int:pk>/',views.seller_delete_product,name='seller-delete-product'),
    path('seller-view-laptop/',views.seller_view_laptop,name='seller-view-laptop'),
    path('seller-view-camera/',views.seller_view_camera,name='seller-view-camera'),
    path('seller-view-accessories/',views.seller_view_accessories,name='seller-view-accessories'),

    path('ajax/validate_email/',views.validate_email,name='validate_email'),
    path('ajax/validate_oldpassword/',views.validate_oldpassword,name='validate_oldpassword'),
    # path('ajax/validate_newpassword/',views.validate_newpassword,name='validate_newpassword'),
    path('ajax/validate_product_name/',views.validate_product_name,name='validate_product_name'),
]