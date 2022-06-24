from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Cluster(models.Model):
    name = models.CharField(max_length=64)
    parent_cluster = models.ForeignKey(
        "Cluster", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    content = models.FileField(
        upload_to="source-content/",
        validators=[FileExtensionValidator(allowed_extensions=["md"])],
        null=True,
        blank=True,
    )
    cluster = models.ForeignKey(
        Cluster, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.body[:32]
