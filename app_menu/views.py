from django.shortcuts import render
from .models import Menu


def draw_menu(request, menu_name):
    menu = Menu.objects.get(name=menu_name)
    return render(request, 'app_menu/menu.html', {'menu': menu})