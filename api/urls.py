from django.urls import path,re_path
from .views import example_view

urlpatterns = [
    path('example/<int:id>', example_view),
    path('example/', example_view)

]
