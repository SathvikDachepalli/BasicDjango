from django.urls import path
from . import views

urlpatterns = [
    # Path Conversters
    # int:numbers
    # str:strings
    # path:wholeurls/
    # slug : Hypen - and underscores_stuff
    # UUID: universally unique indentifier
    path("", views.home, name="home"),
    path("<int:year>/<str:month>/", views.home, name="home"),
]
