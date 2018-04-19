from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^translate/', include('translate.urls')),
    url(r'^index/', include('translate.urls')),
    url(r'^', include('translate.urls')),
]

