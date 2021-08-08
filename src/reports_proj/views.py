from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def Login(request):
    form =  AuthenticationForm()
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password=password)
            if user is not None:
                login(request,user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))

                else:
                    return redirect('sales:home')    

    context = {
        'form':form,
    
    }
    return render(request,'auth/login.html',context)

def Logout(request):
    logout(request)
    return redirect('login')