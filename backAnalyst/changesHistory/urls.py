from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import ChangesHistoryViewSet

router = DefaultRouter()
router.register(r'changes_history', ChangesHistoryViewSet, basename='changes_history')
urlpatterns = router.urls