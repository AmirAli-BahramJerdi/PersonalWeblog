from django.urls import path
from .views import homepage, project_detail

app_name = 'homepage'
urlpatterns = [
    path(route='', view=homepage, name='homepage_app'),
    path(route='/detail/<int:project_id>/', view=homepage, name='detail'),
    
]

