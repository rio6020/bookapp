from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListBookview.as_view(),name='list-book'),
    path('book/',views.ListBookview.as_view(), name='list-book'),
    path('book/create/',views.CreateBookView.as_view(), name='create-book'),
    path('book/<int:pk>/update/',views.UpdateBookView.as_view(), name='update-book'),
    path('book/<int:pk>/delete/',views.DeleteBookView.as_view(),name='delete-book'),

]