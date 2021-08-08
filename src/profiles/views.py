from django.shortcuts import render
from profiles.models import Profile
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def my_profile_view(request):
    user_profile =Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=user_profile)
    flag = False
    context ={}

    if form.is_valid():
        form.save()
        flag = True
        print("profile has been updated")

    context={
        'flag':flag,
        'profile':user_profile,
        'form':form,
    }    
    return render(request, 'profiles/main.html',context)