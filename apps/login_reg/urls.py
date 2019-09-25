from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^log_out$', views.log_out),
    url(r'^user_profile$', views.user_profile, name='user_profile'),
    url(r'^login$', views.login),
    url(r'^register', views.register),
    url(r'^$', views.login_reg),
]