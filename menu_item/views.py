from django.views.generic import ListView

from menu_item.models import MenuItem


class BaseContextView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.kwargs.get('title')
        return context


class MenuView(BaseContextView):
    """Класс представления меню в шаблоне."""

    model = MenuItem
    template_name = "menu_item/test_menu.html"
    context_object_name = "menu_item"
