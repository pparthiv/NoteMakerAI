from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Note
from .forms import createForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    notes = Note.objects.filter(user = request.user)
    return render(request, "notes.html", {'notes': notes})

@login_required
def description(request, id):
    note = get_object_or_404(Note, pk=id)
    return render(request, "desciptionBlock.html", {'note': note})

@login_required
def create(request):
    if request.POST:
        form = createForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect(index)
    return render(request, 'create.html', {'form' : createForm})

@login_required
def edit(request, id):
    note = get_object_or_404(Note, pk=id)
    form = createForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect(description, id)
    return render(request, 'edit.html', {'form': form, 'notes': note})

@login_required
def delete(request, id):
    note = get_object_or_404(Note, pk=id)
    note.delete()
    return redirect(index)