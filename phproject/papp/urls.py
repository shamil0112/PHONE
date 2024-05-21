from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name="home"),
    path('table',views.table,name="table"),
    path('main',views.main, name='main'),
    path("delete/<id>",views.Delete_contact,name="dalete_contact"),
    path('edit/<int:pk>/', views.edit_person, name='edit_person'),
    
]