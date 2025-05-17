from django import template
from django.db import connection
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def draw_menu(title_menu: str):
    """ Прямой запрос в БД получаем объект и весь корневой каталог меню до главного."""
    with connection.cursor() as cursor:
        query = """
        WITH RECURSIVE parent_hierarchy AS (
            SELECT id, title, parent_id
            FROM menu_item_menuitem
            WHERE title = %s

            UNION ALL

            SELECT m.id, m.title, m.parent_id
            FROM menu_item_menuitem m
            JOIN parent_hierarchy ph ON m.id = ph.parent_id
        ),
        submenus AS (
            SELECT id, title, parent_id
            FROM menu_item_menuitem
            WHERE parent_id = (SELECT id FROM menu_item_menuitem WHERE title = %s)
        )
        SELECT * FROM parent_hierarchy
        UNION ALL
        SELECT * FROM submenus;
        """
        cursor.execute(query, [title_menu, title_menu])
        results = cursor.fetchall()
        results = {row[0]: {'id': row[0], 'title': row[1], 'parent_id': row[2]} for row in results}

        return generate_menu(results, title_menu)


def generate_menu(items: dict, title_menu: str):
    if not items:
        return None

    hierarchy_menu = sorted(items.items(), key=lambda item: item)  # Сортируем объекты от корневого меню
    hierarchy_menu_iter = iter(hierarchy_menu)  # Итератор для удобства вывода объектов в html

    ul = '<ul>'
    for i in range(len(hierarchy_menu)):
        title = next(hierarchy_menu_iter)[1]['title']  # Достаем следующий объект из итератора
        if title == title_menu:
            ul += f'<li><a href="/{title}/">{title}</a><ul>'
            try:
                while True:
                    title = next(hierarchy_menu_iter)[1]['title']  # Выводим первый уровень вложенности подменю.
                    ul += f'<li><a href="/{title}/">{title}</a></li>'
            except StopIteration:
                break
        ul += f'<li><a href="/{title}/">{title}</a>'
        ul += '<ul>'

    return format_html(ul)
