from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("",bookView),
    path("add-book/",addBookView),
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit", editBook),
    path("delete-book", deleteBookView),
]
