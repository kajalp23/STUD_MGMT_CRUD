from django.urls import path,include
from student import views

urlpatterns = [
    path('update/<int:up_id>/',views.update,name="update"),
    path('delete/<int:my_id>/',views.delete,name="delete"),
    # path('show/',views.show,name="show"),
]