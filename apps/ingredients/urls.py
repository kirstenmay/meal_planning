from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^find_recipe$', views.find_recipe),
    url(r'^add_ingredient$', views.add_ingredient),
    url(r'^$', views.ingredient),

]