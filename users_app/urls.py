from django.urls import path, include
from users_app.views import *

urlpatterns = [
    path('register/', UsersView.as_view(),name='register'),
    path('me/<str:FOR>/', UsersDataView.as_view(),name='users_q_s'),
]
