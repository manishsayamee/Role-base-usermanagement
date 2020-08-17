from django.urls import path
from .views import uploadfile_createView, uploadfile_listView, detailview, updateview, deleteview

app_name='files'
urlpatterns = [
  path('create/',uploadfile_createView.as_view(),name='create' ),
  path('list/',uploadfile_listView.as_view(),name='list' ),
  path('detail/<int:pk>/', detailview ,name='detail'),
  path('update/<int:pk>/', updateview.as_view() ,name='update'),
  path('delete/<int:pk>/', deleteview.as_view(),name='delete'),
  # path('try/', tryself.as_view(), name='try'),



]