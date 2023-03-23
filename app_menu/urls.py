from django.urls import path
from app_menu.views import draw_menu

app_name = 'app_menu'

urlpatterns = [
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]