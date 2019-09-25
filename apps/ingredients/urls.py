from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.ingredient),
    url(r'^add_ingredient$', views.add_ingredient),

]