from django.urls import path
from .views import *

urlpatterns = [
    path("say_hello/", say_hello),
    path("user_profile/", user_profile),
    path('record/<int:query_id>/', filter_queries, name='filter_queries')
]
