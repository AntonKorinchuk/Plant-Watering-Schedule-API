from rest_framework.routers import DefaultRouter

from plants.views import PlantViewSet


router = DefaultRouter()
router.register("plants", PlantViewSet)

urlpatterns = router.urls

app_name = "plants"
