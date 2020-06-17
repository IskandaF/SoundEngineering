from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpRequest

from django.shortcuts import render,redirect
from .forms import ProjectForm,AddTracksForm
from .models import Project,Track

@login_required
def CreateProject(request):
    form=ProjectForm(request.POST or None)
    context={"form":form}
    if request.method == "POST":
        if form.is_valid():
            project=Project()
            project.user=request.user
            project.name=form.cleaned_data["name"]
            project.save()
            return redirect("/")

    return render(request,"create_project.html",context)

def EditProject(request,project_id):
    project=Project.objects.get(id=project_id)
    projectform=ProjectForm(request.POST or None,prefix="project", instance=project)
    tracks=Track.objects.filter(project=project_id)
    addtrackform=AddTracksForm(request.POST or None,prefix="track",initial={"project":project})

    if request.method == "POST":
        if projectform.is_valid():
            projectform.save()
            # return HttpResponseRedirect(request.path_info)
        if addtrackform.is_valid():
            track=Track()
            track.name=addtrackform.cleaned_data["name"]
            track.project=Project.objects.get(id=project_id)
            track.save()
            addsuccess=("Track added")
            return HttpResponseRedirect(request.path_info,addsuccess)
    context={"projectform":projectform,"addtrackform":addtrackform,"tracks":tracks}


    return render(request,"edit_project.html",context)
    
def DeleteProject(request,project_id):
    project=Project.objects.get(id=project_id)
    project.delete()
    return redirect("/")

    


# Create your views here.
