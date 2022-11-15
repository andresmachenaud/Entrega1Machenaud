from django.urls import path
from applibreria.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
]