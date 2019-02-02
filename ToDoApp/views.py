from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoItem
# Create your views here.
def todoView(request):
    all_todo_items=ToDoItem.objects.all()
    return render(request,'todo.html',{'all_items':all_todo_items})

def add_todo(request):
    new_item = ToDoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
def delete_todo(request, todo_id):
    item_to_delete = ToDoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')