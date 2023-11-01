from . import views
from django.urls import path

urlpatterns = [
    path('', view=views.test, name='test')
]
