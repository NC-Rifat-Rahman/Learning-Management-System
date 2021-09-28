from django.conf.urls import url
from django.urls import path, include
from accounts import views
from .views import userPostAPIiew, userPostRudView,LoginAPIView

app_name = 'accounts'
urlpatterns = [
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    url(r'^$', userPostAPIiew.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', userPostRudView.as_view(), name='post-rud'),
    path('login/', views.LoginAPIView.as_view(), name="login"),
]
