from django.urls import path, include
from .views import CatsEveryWhereList, DeleteDataView, AddDataView, EditDataView

urlpatterns = [
    path('', CatsEveryWhereList.as_view(), name = 'cats-everywhere-list'),
    path('add/', AddDataView.as_view(), name = 'cats-everywhere-add'),
    path('<int:pk>/delete/', DeleteDataView.as_view(), name = 'delete-data'),
    path('<int:pk>/edit/', EditDataView.as_view(), name = 'edit-data'),
]