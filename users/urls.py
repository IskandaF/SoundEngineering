from django.urls import path

from users.views import login_view,register_view,logout_view
app_name = 'users'
urlpatterns=[
    path("",login_view),
    path("register/",register_view,name="register"),
    path("logout/",logout_view,name="logout")
]