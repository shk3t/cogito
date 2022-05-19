from django.shortcuts import render
from base.models import Cluster


def cluster(request, cluster_id):
    cluster = Cluster.objects.get(id=cluster_id)
    context = {"cluster": cluster}
    return render(request, "base/cluster.html", context)
