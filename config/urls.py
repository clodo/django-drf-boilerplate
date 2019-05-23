from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('api/v1/', include('project.api.urls')),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
