from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from categories import views as category_views

router = routers.DefaultRouter()
router.register(r'categories', category_views.CategoryView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
    path('api/', include(router.urls)),
]
