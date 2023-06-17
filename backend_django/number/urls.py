from django.contrib import admin
from django.urls import path

from .views import (segitiga, prima, ganjil)

urlpatterns = [
    path("segitiga/<int:number>", segitiga),
    path("ganjil/<int:number>", ganjil),
    path("prima/<int:number>", prima),
]
