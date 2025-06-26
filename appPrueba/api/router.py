from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet, SuscripcionViewSet

router = DefaultRouter()
router.register(prefix='articulo', basename='articulo', viewset=ArticuloViewSet)
router.register(prefix='suscritor', basename='suscritor', viewset=SuscripcionViewSet)


