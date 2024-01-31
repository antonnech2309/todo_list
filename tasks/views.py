from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"

    def post(self, request, *args, **kwargs):
        if 'task_pk' in request.POST:
            task = Task.objects.get(pk=request.POST['task_pk'])
            task.is_completed = not task.is_completed
            task.save()
        return super().get(request, *args, **kwargs)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")

