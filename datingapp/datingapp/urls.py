from django.contrib import admin
from django.urls import path, include

from clients.views import ClientViewSet, LoginUser, ClientListAPIView
from clients.yasg import urlpatterns as doc_urls

from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list/', ClientListAPIView.as_view()),
    path('api/clients/create', ClientViewSet.as_view({'post': 'create'})),
    path('api/clients/<int:pk>/mathc', ClientViewSet.as_view({'post': 'likes'})),
    path('login/', LoginUser.as_view())
    # path('api/', include(router.urls))
] + doc_urls

# Password123!@#