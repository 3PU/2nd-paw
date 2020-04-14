from django.conf.urls import url, include
from home.views import index
from accounts.views import registration, login, userprofile, logout
from accounts import url_reset

urlpatterns = [
    url(r'^register/$', registration, name="registration"),
    url(r'^login/$', login, name="login"),
    url(r'^profile/$', userprofile, name="userprofile"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^password-reset/', include(url_reset))
]