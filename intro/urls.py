from django.urls import path
from intro import views

urlpatterns = [
    path('first_page/', views.show_name, name='first-page'),
    path('second_page/', views.show_another_name, name='second-page'),
    path('list_of_cars/', views.cars, name='list_for_cars'),
    path('list_of_books/', views.books, name='list_for_books'),
]
