from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from measurements.views import ProjectViewSet, MeasurementViewSet


# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`
router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'measurement', MeasurementViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/project', ProjectViewSet.as_view({'get': 'list'})),
    # path('api/measurement', MeasurementViewSet.as_view({'get': 'list'})),
]
