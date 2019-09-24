from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^add_ingredient$', views.add_ingredient),

]