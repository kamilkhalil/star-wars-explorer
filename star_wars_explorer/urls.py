from django.contrib import admin
from django.urls import path, include

from swapi_collections.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('collection/', include('swapi_collections.urls')),
]
