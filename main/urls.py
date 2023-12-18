from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import auth.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tests.urls')),
    path('', include(auth.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('custom_profile.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
