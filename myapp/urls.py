from django.urls import path

from myapp import models
from . import views

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("contact/add/", views.add_contact, name="add_contact"),
    path("contact/<int:pk>/", views.contact_details, name="contact_details"),
    path("update/<int:pk>/", views.update_contact, name="update_contact"),
    path("delete/<int:pk>/", views.delete_contact, name="delete_contact"),
]
