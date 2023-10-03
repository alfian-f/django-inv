from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_json_by_id, show_xml_by_id, register, login_user, logout_user, delete_item
from main.views import edit_item, increment_item, decrement_item
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('increment/<int:id>', increment_item, name='increment_item'),
    path('decrement/<int:id>', decrement_item, name='decrement_item')
]