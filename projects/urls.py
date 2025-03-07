from rest_framework import routers
from projects.api import ProjectViewSet

routers = routers.DefaultRouter()

routers.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = routers.urls