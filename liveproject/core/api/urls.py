from django.urls import path
from .views import customuserlistcreate, customuserupdate

urlpatterns = [
    path('customuser/', customuserlistcreate, name='customuser-create'),
    path('customuser/<int:pk>', customuserupdate, name='customuserupdate'),
]
