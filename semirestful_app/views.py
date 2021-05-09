from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows')

def show(request):
    context = {
        "all_shows" : Show.objects.all()
    }
    return render(request, "shows.html", context)

def show_new(request):
    return render(request, "new_show.html")

def show_create(request):
    if request.method=="POST":

        errors = Show.objects.validator(request.POST)

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)

            return redirect(f"/shows/new")

        show=Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])

        return redirect(f"/shows/{show.id}")

    return redirect('/shows/new')

def show_show(request, id):
    context = {
        'this_show' : Show.objects.get(id=id)
    }
    return render(request, "specific_show.html", context)

def show_edit(request, id):
    context = {
        'this_show' : Show.objects.get(id=id)
    }
    return render(request, "edit_show.html", context)

def show_update(request, id):
    if request.method == "POST":

        errors = Show.objects.edit_validator(request.POST)

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)

            return redirect(f"/shows/{id}/edit")

        this_show = Show.objects.get(id=id)
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release_date = request.POST['release_date']
        this_show.description = request.POST['description']
        
        this_show.save()
    return redirect(f'/shows/{id}')


def show_destroy(request, id):
    if request.method == "POST":
        this_show = Show.objects.get(id=id)
        this_show.delete()

    return redirect('/shows')