from django.urls import path
from . import views
from .views import RevisionDetail

app_name="revisions"
urlpatterns=[
    path("", views.dashboard,name="dashboard"),
    path("<int:project_id>/add_revision/",RevisionDetail,name="add_revision"),
    
]