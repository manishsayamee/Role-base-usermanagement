from django.urls import path
from .views import uploadfile_createView, uploadfile_listView, commentview, updateview, deleteview

app_name='files'
urlpatterns = [
  path('create/',uploadfile_createView.as_view(),name='create' ),
  path('list/',uploadfile_listView.as_view(),name='list' ),
  path('comment/<int:pk>/', commentview,name='comment'),

  path('update/<int:pk>/', updateview ,name='update'),
  path('delete/<int:pk>/', deleteview,name='delete'),



]