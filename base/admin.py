from django.contrib import admin

from .models import Cluster, Source, Message

admin.site.register(
    [
        Cluster,
        Source,
        Message,
    ]
)
