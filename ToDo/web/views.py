from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView, DeleteView, UpdateView, DetailView
from .models import Task
from bootstrap_datepicker_plus import DateTimePickerInput

# def mylist(request):
#     return render(request,'web/mylist.html')
# Create your views here.

class TaskView(View):

    def get(self,request):
        # TODO: check user authenticated
        if request.user.is_authenticated:
            tasks=Task.objects.filter(user=request.user)
            return render(request,'mytasks.html',{'tasks':tasks})
        else:
            redirect('home')

class TaskCreateView(CreateView):
    model = Task
    fields = ['title','text','priority','level','due_date']
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        user=self.request.user
        form.instance.user=user
        return super(TaskCreateView,self).form_valid(form)
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'web/task_delete.html'
    success_url = reverse_lazy('home')




class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'web/task_update.html'
    fields = ['title','text','priority','level','due_date']

    success_url = reverse_lazy('home')

# class TaskDetailView(DetailView):
#     model = Task
#     template_name = 'web/task_detail.html'
