from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beyondthearc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^statistics/', include('statistics.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact', TemplateView.as_view(template_name='contact.html'),name='contact'),
    url(r'^home', TemplateView.as_view(template_name='home.html'),name='home'),
)
