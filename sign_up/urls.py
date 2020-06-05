from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sign_up import views

urlpatterns = [
    path('sign-up/', views.SignUp.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)