from django.contrib import admin

from base.models import Cluster, Source, Message

admin.site.register(
    [
        Cluster,
        Source,
        Message,
    ]
)
