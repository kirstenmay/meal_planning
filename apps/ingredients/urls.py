from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^search_recipe$', views.search_recipe),
    url(r'^select_ingredient$', views.select_ingredient),
    url(r'^api/ing_search$', views.dynamic_search),
    url(r'^find_recipe$', views.find_recipe),
    url(r'^add_ingredient$', views.add_ingredient),
    url(r'^$', views.ingredient),

]