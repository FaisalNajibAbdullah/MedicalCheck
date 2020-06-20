from django.conf.urls import url, include
from django.contrib import admin
from check import views

urlpatterns = [
	url(r'^check/', include('check.urls',namespace = 'check')),
    url(r'^admin/', admin.site.urls),
    url(r'captcha/', include('captcha.urls'))
]
