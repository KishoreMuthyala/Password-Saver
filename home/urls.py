from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<int:id>', views.delete, name="delete"),
    path('update/<int:id>/<str:val>', views.update, name="update"),
    path('search/<int:id>', views.search, name="search"),
]
