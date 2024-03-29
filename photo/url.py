from django.urls import path
from .views import PhotoList, PhotoDelete, PhotoDetail, PhotoUpdate,PhotoCreate

app_name = "photo"

urlpatterns = [
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", PhotoDetail.as_view(), name='detail'),
    path("", PhotoList.as_view(), name='index'),
]