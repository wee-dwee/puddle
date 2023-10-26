from django.shortcuts import render,get_object_or_404,redirect
from .models import items,Category
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def it(request):
    query=request.GET.get('query','')
    categories=Category.objects.all()
    category_id=request.GET.get('category',0)
    item=items.objects.filter(is_sold=False)

    if category_id:
        item=item.filter(category_id=category_id)

    if query:
        item=item.filter(Q(name__icontains=query) | Q(desc__icontains=query))

    return render(request,'item/items.html',{
        'items':item,
        'query':query,
        'categories':categories,
        'category_id':int(category_id)
    })

@login_required
def detail(request,pk):
    item= get_object_or_404(items,pk=pk)
    related_items=items.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
        'item':item,
        'related_items':related_items
    })

@login_required
def new(request):
    if request.method=='POST':
        form=Newitemform(request.POST,request.FILES)
        if form.is_valid():
            i=form.save(commit=False)
            i.created_by=request.user
            i.save()
            return redirect('item:detail',pk=i.id)
    else:
        form=Newitemform()
    return render(request,'item/form.html',{
        'form':form
    })

@login_required
def delete(request,pk):
    item= get_object_or_404(items,pk=pk)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    item= get_object_or_404(items,pk=pk)
    if request.method=='POST':
        form=Edititemform(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form=Edititemform(instance=item)
    return render(request,'item/form.html',{
        'form':form
    })