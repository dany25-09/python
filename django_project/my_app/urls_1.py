from django.urls import path 
from my_app.views import hello, about

urlpatterns = [
    path("", hello),
    path("about/", about)
]