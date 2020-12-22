from rest_framework.routers import DefaultRouter
from . import viewsets

app_name = "rest_api"
router = DefaultRouter()

router.register("users", viewsets.UserViewSet)
router.register("permissions", viewsets.PermissionViewSet)
router.register("groups", viewsets.GroupViewSet)

urlpatterns = router.urls
