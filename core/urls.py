from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import pages.products_url
import accounts.urls
from pages.views import IndexView, shablon_view, render_cars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('shablon/', shablon_view, name='shablon'),
    path('cars/', render_cars, name='cars'),
    path('products/', include(pages.products_url)),
    path('accounts/', include(accounts.urls))
    # path('', image),
    # path('', TemplateView.as_view(template_name='index.html')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
