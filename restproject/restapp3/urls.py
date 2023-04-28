from django.urls import path
from .import views
app_name='restapp3'

urlpatterns = [

    path('indexop',views.indexop,name='indexop'),
    path('food/<int:food_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:food_id>/',views.update,name='update'),
    path('delete/<int:food_id>/',views.delete,name='delete'),
    
]