from django.urls import path, include
from auth_app.views import *

urlpatterns = [
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
]
