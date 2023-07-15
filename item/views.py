from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def browse(request):
    items=item.objects.filter(is_sold=False)
    query=request.GET.get('query','')
    category_id=request.GET.get('category',0)
    categories=category.objects.all()

    if category_id:
        items=items.filter(category_id=category_id)

    if query:
        items=items.filter(Q(name__icontains=query)|Q(description__icontains=query)) #insensitive case
    return render(request,'item/browse.html',{'items':items,'query':query,'categories':categories,'category_id':int(category_id)})

# Create your views here.
def detail(request, pk):
    items=get_object_or_404(item,pk=pk)
    related_items=item.objects.filter(category=items.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{'item': items,'related_items':related_items})

@login_required
def new(request):
    if request.method=='POST':
        form=newitemform(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)
            
    else:   
        form=newitemform()

    return render(request,'item/form.html',{
        'form':form,
        'title':'New Item'
    })

@login_required
def delete(request,pk):
    items=get_object_or_404(item,pk=pk,created_by=request.user)
    items.delete()

    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    items=get_object_or_404(item,pk=pk,created_by=request.user)

    if request.method=='POST':
        form=edititemform(request.POST,request.FILES,instance=items)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=items.id)
            
    else:   
        form=edititemform(instance=items)

    return render(request,'item/form.html',{
        'form':form,
        'title':'Edit Item'
    })