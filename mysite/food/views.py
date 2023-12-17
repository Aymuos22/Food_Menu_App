from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Item
from  django.template import loader
from .forms import ItemForm
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

def index(request):
    item_list=Item.objects.all()
    context={
        'item_list': item_list,
    }
    return render(request,'food/index.html',context)
def item(request):
    return HttpResponse('<h1>Item View</h1>')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item
    }
    return render(request,'food/detail.html',context)

from django.urls import reverse_lazy

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        # Redirect to the 'index' URL after successfully saving the item
        return reverse_lazy('food:index')  # Replace 'index' with the name used in your URL configuration



    
@login_required
def update_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        # Handle the case where the item with the given ID doesn't exist
        return HttpResponse("Item not found", status=404)

    form = ItemForm(request.POST, request.FILES, instance=item)


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("successful")
            return redirect('food:index')  # Redirect to the index upon successful update
    print("unsuccessful")
    print(form.errors)
    return render(request, 'food/item_form.html', {'form': form, 'item': item})

@login_required
def delete_item(request,item_id):
    item=Item.objects.get(id=item_id)
    
    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})