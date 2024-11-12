from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from .models import (
    Profile, Message, Project
)


def homepage(request): 

    projects = Project.objects.all()
    profile = Profile.objects.all().last()
    

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Message.objects.create(
                lname=cd['lname'],
                fname=cd['fname'],
                email=cd['email'],
                phone_number=cd['phone_number'],
                service_type=cd['service_type'],
                message=cd['message']
            )
            messages.success(request=request, message='پیام شما با موفقیت ارسال شد', extra_tags='success')
            return redirect('homepage:homepage_app')
        else:
            messages.error(request=request, message='پیام شما ارسال نشد', extra_tags='dnager')
    else:
        
        form = ContactForm()

    return render(request, 'homepage/index.html',{
        'profile':profile, 
        'form':form, 
        'projects':projects
    })


def project_detail(request, project_id):
    
    project = get_object_or_404(Project, id=project_id)
    previous_project = Project.objects.filter(id__lt=project_id).order_by('-id').first()
    next_project = Project.objects.filter(id__gt=project_id).order_by('id').first()
    
    return render(request, 'homepage/project_detail.html', {
        'project': project,
        'previous_project': previous_project,
        'next_project': next_project,
    })
