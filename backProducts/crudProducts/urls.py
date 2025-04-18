from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()
router.register('api/crudProducts', ProductViewSet, 'crudProducts')
urlpatterns = router.urls