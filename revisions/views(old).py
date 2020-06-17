from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Revision
from django.contrib.auth.decorators import login_required
from .forms import GeneralForm
from django.forms import formset_factory
from tracks.models import Project,Track

@login_required
def dashboard(request):
    projects=Project.objects.filter(user=request.user)
    context={
        "projects":projects,
    }
    return render(request,"revisions/dashboard.html",context)

def RevisionDetail(request,project_id):
    tracks = Track.objects.filter(project=project_id)  
    project=Project.objects.get(id=project_id)
    
    formset=formset_factory(form=GeneralForm,extra=len(tracks))
    

    # ziplist=zip(formset,tracks)
    template_name="revisions/add_revision.html"
    context={
        
        "tracks":tracks,
        # "formset_tracks":ziplist,
        "formset":formset(),
        "project":project_id,


    }

    if request.method =="POST":

        if formset.is_valid():
            message={}
            for form in formset:
                for i in form:
                    message[i]=
                form.save()

        else:
            return HttpResponse("Please enter valid values")


    return render(request,template_name,context)

# Create your views here.
