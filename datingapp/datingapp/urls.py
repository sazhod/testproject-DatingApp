from django.contrib import admin
from django.urls import path, include

from clients.views import ClientViewSet
from clients.yasg import urlpatterns as doc_urls

from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients/', ClientViewSet.as_view({'get': 'list'})),
    path('api/clients/create', ClientViewSet.as_view({'post': 'create'})),
    # path('api/', include(router.urls))
] + doc_urls
