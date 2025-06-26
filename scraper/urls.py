from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_form, name="job_form"),
    path("jobs/", views.job_list, name="job_list"),
]