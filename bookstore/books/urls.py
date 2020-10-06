from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.categ, name='categ'),
    path('<str:name>/detail', views.detail, name='detail'),

]
