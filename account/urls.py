from django.urls import path
from .views import *
app_name = 'account'
urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('activation-pending/', activation_pending, name='activation_pending'),
    path('logout/', logout, name='logout'),
]
