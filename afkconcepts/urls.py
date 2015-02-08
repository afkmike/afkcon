from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
import views
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'afkconcepts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace='home')),#www.afkovertime.com will point nto afkovertime.com/home/
    url(r'^home.htm', views.index, name="home"),
    url(r'^services.htm', views.services, name="services"),
    url(r'^contact.htm', views.contact, name="contact"),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',

        'serve',
        {'document_root': settings.MEDIA_ROOT}),

    )
