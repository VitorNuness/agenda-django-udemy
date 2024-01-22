from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('<int:id>/', views.show, name='show'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
