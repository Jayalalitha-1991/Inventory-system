# inventory/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Step 1: Create a router object
router = DefaultRouter()

# Step 2: Register your viewsets with the router
router.register(r'products', ProductViewSet)   # Handles CRUD for products
# router.register(r'suppliers', SupplierViewSet) # Handles CRUD for suppliers
# router.register(r'sales', SaleViewSet)         # Handles CRUD for sales

# Step 3: Include router URLs along with any custom paths
urlpatterns = [
    path('', include(router.urls)),  # All the router URLs (like products/, suppliers/, etc.)
    # path('sales-report/', sales_report, name='sales-report'),  # Custom URL for sales report
]
