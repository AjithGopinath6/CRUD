from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    path('insertData',views.insertData,name="insertData"),
    path('updateData/<id>',views.updateData,name="updateData"),
    path('deleteData/<id>',views.deleteData,name="deleteData"),
]
