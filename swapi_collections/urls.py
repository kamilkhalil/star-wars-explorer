from django.urls import path

from . import views


urlpatterns = [
    path("<int:collection_id>", views.collection_detail, name="detail"),
]
