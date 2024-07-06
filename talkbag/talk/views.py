from django.shortcuts import render,redirect
from .models import Talk
from .forms import talkForm,userRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')


def talk_list(request):
    query=request.GET.get("q")
    if query:
        talks= Talk.objects.filter(text__icontains=query)
    else:
        talks=Talk.objects.all().order_by('-created_at')
    return render(request,'talk_list.html',{'talks':talks})

    
    

@login_required
def talk_create(request):
    if request.method=="POST":
        form=talkForm(request.POST, request.FILES)
        if form.is_valid():
            talk=form.save(commit=False)
            talk.user=request.user
            talk.save()
            return redirect('talk_list')
    else:
        form=talkForm()
    return render(request, 'talk_form.html',{'form':form})
    
@login_required   
def talk_edit(request,talk_id):
    talk=get_object_or_404(Talk,pk=talk_id,user=request.user) 
    if request.method=="POST":
        form=talkForm(request.POST, request.FILES,instance=talk)
        if form.is_valid():
            talk_=form.save(commit=False)
            talk_.user=request.user
            talk_.save()
            return redirect('talk_list')
    else:
        form=talkForm(instance=talk)
    return render(request, 'talk_form.html',{'form':form})

@login_required
def talk_delete(request,talk_id):
    talk=get_object_or_404(Talk,pk=talk_id, user=request.user)
    if request.method=='POST':
        talk.delete()
        return redirect('talk_list')
    return render(request, 'talk_confirm_delete.html',{'talk':talk})

def register(request):
    if request.method=="POST":
        form=userRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('talk_list')
    else:
        form=userRegistrationForm()
    return render(request, 'registration/register.html',{'form':form})


