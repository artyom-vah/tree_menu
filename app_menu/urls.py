from django.urls import path
from .views import draw_menu

urlpatterns = [
    path('<menu_name>/', draw_menu, name='menu'),
]

