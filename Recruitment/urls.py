from django.urls import path, include
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('', include('Evaluator.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
