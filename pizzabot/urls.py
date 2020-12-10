from django.contrib import admin
from django.urls import path

from bot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.land),
    path('save/', views.saveOrder),
    path('checkstatus/', views.checkStatus)
]
