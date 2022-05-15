from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    #path("cluster/<int:cluster_id>/", views.cluster, name="cluster"),
    path("sources/", views.source_list, name="source-list"),
    path("source/create", views.create_source, name="create-source"),
    path("source/<int:source_id>/", views.source, name="source"),
    path("source/<int:source_id>/create-message", views.create_message, name="create-message"),
    path("global-chat/", views.global_chat, name="global-chat"),
]
