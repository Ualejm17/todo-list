from django.urls import path
# ^importar el path para poder crear las urls
from .views import TaskListView
# ^importar la vista que acabamos de crear


urlpatterns = [
# ^lista de urls de la aplicacion tasks
    path('', TaskListView.as_view(), name='task-list'),
# ^asociar la vista con la url
# ^crear la url, el primer argumento es la url, el segundo es la vista que se va a llamar
    

]