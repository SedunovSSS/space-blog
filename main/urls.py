from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view),
    path('login', login_frontend),
    path('login_backend', login_backend),
    path('logout', logout_backend),
    path('register', register_frontend),
    path('register_backend', register_backend),
    path('add_post', add_frontend),
    path('add_backend', add_backend),
    path('view', view),
]
