from django.urls import include, path
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
