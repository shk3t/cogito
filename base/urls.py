from django.urls import path

from base.views import home, auth, user, source, message


urlpatterns = [
    # Home
    path("", home.blank),
    path("home", home.home, name="home"),

    # Authentication
    path("login", auth.login_view, name="login"),
    path("logout", auth.logout_view, name="logout"),
    path("register", auth.register_view, name="register"),

    # Users
    path("profile/<int:user_id>", user.get_user_info, name="profile"),

    # Sources
    path("sources", source.list_sources, name="source-list"),
    path("source/create", source.create_source, name="create-source"),
    path("source/<int:source_id>/update", source.update_source, name="update-source"),
    path("source/<int:source_id>", source.get_source, name="source"),
    path("source/<int:source_id>/delete", source.delete_source, name="delete-source"),

    # Messages
    path("source/<int:source_id>/create-message", message.create_message, name="create-message"),
    path("global-chat", message.get_all_messages, name="global-chat"),
    path("global-chat/<int:page>", message.get_all_messages, name="global-chat"),
]
