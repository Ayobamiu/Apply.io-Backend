from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from user.views import UserViewSet, ProfileViewSet
from competition.views import CompetitionViewSet
from entry.views import EntryViewSet

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)
router.register('entry', EntryViewSet)
router.register('competition', CompetitionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api/', include(router.urls)),
    path('api/', include('user.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
