from django.conf.urls import url
from . import views

# all urls on this app start with "recipes/"

urlpatterns = [
    url(r'^add_recipe$', views.add_recipe),
    url(r'^new_recipe$', views.new_recipe),
    url(r'^view_recipe/(?P<id>\d+)$', views.view_recipe, name="view_recipe"),
]