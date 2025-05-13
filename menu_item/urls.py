from django.urls import path

from menu_item.apps import MenuItemConfig
from menu_item.views import MenuView

app_name = MenuItemConfig.name

urlpatterns = [
    path("", MenuView.as_view(), name="menu_view"),
]
