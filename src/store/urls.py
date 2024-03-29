from django.urls import path
from rest_framework_nested import routers
from . import views

# URLConf
router = routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('collection',views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet,basename='orders')

product_router = routers.NestedSimpleRouter(router, 'products',lookup='product')
product_router.register('reviews',views.ReviewViewSet,basename='product-reviews')

cart_router = routers.NestedSimpleRouter(router,'carts', lookup='cart')
cart_router.register('items',views.CartItemViewSet,basename='cart-items-detail')

urlpatterns = router.urls + product_router.urls + cart_router.urls