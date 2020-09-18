from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='myapp-food'),
    path('delete/<int:id>', views.delete_consume, name='myapp-delete'),

]
