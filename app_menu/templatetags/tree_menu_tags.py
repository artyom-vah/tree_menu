from django import template
from app_menu.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    '''Отображает(рендерит) меню с указанным названием.'''
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return ''

    request = context['request']
    current_path = request.path

    def is_active(item):
        return current_path.startswith(item.url)

    def draw_item(item):
        return template.Template('{% include "app_menu/menu_item.html" %}').render({
            'item': item,
            'is_active': is_active(item),
            'draw_item': draw_item,
        })

    return template.Template('{% include "app_menu/menu.html" %}').render({
        'menu': menu,
        'draw_item': draw_item,
    })
