from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.actions.views import StartActionAPI, StopActionAPI
from apps.authentication.views import UserViewSet
from apps.inventory.views import SellItemView
from apps.items.views import ItemViewSet
from apps.merchants.views import BuyItemView
from apps.state.views import UserStateAPI

router = DefaultRouter()
router.register('items', ItemViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/start-action/', StartActionAPI.as_view(), name='start-action'),
    path('api/stop-action/', StopActionAPI.as_view(), name='stop-action'),
    path('api/me/', UserStateAPI.as_view(), name='user-state'),
    path('api/sell-item/', SellItemView.as_view(), name='sell-item'),
    path('api/buy-item/', BuyItemView.as_view(), name='buy-item'),
]
