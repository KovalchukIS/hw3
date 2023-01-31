from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from django.views.generic import (
    CreateView,
    ListView,
    View,
    UpdateView,
    DeleteView,
    DetailView,
)
from todo.models import List


class ListListView(ListView):
    """Представление для отображения множества корзин.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
    """

    context_object_name = "lists_"
    queryset = List.objects.filter(is_done=False)
    # model = Cart
    template_name = "tasks_list.html"


class ListDetailView(DetailView):

    context_object_name = "list"
    queryset = List.objects
    template_name = "Task_detail.html"

    # context_object_name = 'list'
    # queryset = List.objects.filter(is_done=False)
    # # model = Cart
    # template_name = "tasks_list.html"


class ListCreateView(CreateView):
    """Представление для создания одной корзины."""

    model = List
    fields = ["name", "is_done"]
    template_name = "Task_create.html"
    success_url = "/tasks/active"


class ListUpdateView(UpdateView):
    model = List
    fields = ["name", "is_done"]
    template_name = "Task_update.html"
    # template_name_suffix = '_update_form'
    success_url = "/tasks/active"


class ListDeleteView(DeleteView):
    model = List
    success_url = "/tasks/active"
    template_name = "Task_del.html"
