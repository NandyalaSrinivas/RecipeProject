from django.shortcuts import render, redirect, get_object_or_404
from recipeapp.forms import RecipeForm
from recipeapp.models import RecipeModel
from django.urls import reverse

# Create your views here.
def home(request):
    data = RecipeModel.objects.all()
    return render(request,"recipeapp/home.html", {'data': data})


def create(request):
    if request.method =='POST':
        objcreate = RecipeForm(request.POST, request.FILES)
        if objcreate.is_valid():
            objcreate.save()
            return redirect('/home')
    else:
        objcreate = RecipeForm()
        return render(request, "recipeapp/create.html", {"form":objcreate})

def delete(request, id):
    data = get_object_or_404(RecipeModel, pk=id)
    data.delete()
    return redirect('/home')


def details(request):
    data = get_object_or_404(RecipeModel, pk=id)
    return render(request, "recipeapp/details.html", {'data': data})

