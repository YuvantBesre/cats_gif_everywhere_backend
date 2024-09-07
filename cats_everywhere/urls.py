from django.urls import path, include
from .views import CatsEveryWhereList

urlpatterns = [
    path('', CatsEveryWhereList.as_view(), name = 'cats-everywhere-list'),
]