from django.urls import path

from . import views
app_name = "self_storage_admin"
urlpatterns = [
    path('', views.index, name='index'),
]