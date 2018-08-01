from django.contrib import admin
from django.urls import path, include

from .settings import ConfigClass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]

if ConfigClass.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
