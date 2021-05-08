from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.collection_detail, name="collection"),
]