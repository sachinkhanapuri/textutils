from django.urls import path
# from gym.views import add_data,display,homepage
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("add_data/",views.add_data,name="add_data"),
    path("display/",views.display,name="display"),
    path("display_page/<int:id>",views.display_item,name="display_page"),
]
