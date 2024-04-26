from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    path('insertData',views.insertData,name="insertData"),
    path('updatedata/<id>',views.updateData,name="updatedata"),
    path('deletedata/<id>',views.deleteData,name="deletedata"),
]
