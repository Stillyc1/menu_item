from django import template
from django.utils.html import format_html

from menu_item.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(title_menu):
    menu_obj = MenuItem.objects.get(title=title_menu)
    return generate_menu(menu_obj)


def generate_menu(menu_obj):
    parent = menu_obj.parent
    if not parent:
        ul = '<ul>'
        ul += f'<li>{menu_obj.title}'
        ul += '<ul>'
        print(ul)
        for submenu in menu_obj.submenu.all():
            ul += f'<li>{submenu.title}</li>'
        ul += '</ul>'
        ul += '</li>'
        form_html = format_html(ul)
        print(form_html)
        return form_html
    generate_menu(menu_obj.parent)

    # if menu_obj.parent:
    #     ul += f'<li>{menu_obj.parent.title}<ul>'
    #
    # ul += f'<li>{menu_obj.title}'
    #
    # if menu_obj.submenu.all():
    #     ul += '<ul>'
    #     for submenu in menu_obj.submenu.all():
    #         ul += f'<li>{submenu.title}</li>'
    #     ul += '</ul>'
    # ul += '</ul>'
