from django.urls import path
from .views import CreateProject,EditProject,DeleteProject
app_name="tracks"
urlpatterns=[
    path("create/",CreateProject,name="create"),
    path("<int:project_id>/delete/",DeleteProject,name="delete_project"),
    path("<int:project_id>/edit/",EditProject,name="edit_project")
]