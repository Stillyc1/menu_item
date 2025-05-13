from django.views.generic import ListView

from menu_item.models import MenuItem


class MenuView(ListView):
    """Класс представления меню в шаблоне."""

    model = MenuItem
    template_name = "menu_item/test_menu.html"
    context_object_name = "menu_item"
