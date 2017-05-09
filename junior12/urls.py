"""junior12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from junior12.contato.views import ContactView, contact_success

urlpatterns = i18n_patterns(
    url(_(r'^admin/'), admin.site.urls),
    url(r'^', include('junior12.frontend.urls')),
    url(r'^contato/$', ContactView.as_view(), name='contact'),
    url(r'^contato/sucesso/', contact_success, name='contact_success'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=False
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
