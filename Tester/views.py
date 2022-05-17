from django.shortcuts import render, redirect
from multiprocessing import context
# Create your views here.
from django.contrib.auth.models import User
from Tester.forms import TesterForm




def home(request):
    return render(request, 'tester/home.html')


def tlogin(request):
    return render(request,'tester/tlogin.html')    

def tregister(request):
    form=TesterForm()
    if request.method == 'POST':
        form=TesterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email =form.cleaned_data['email']
            phoneno = form.cleaned_data['phoneno']
            password =form.cleaned_data['password']
            cpassword =request.POST.get['cpassword']

            if password==cpassword:
                user = User.objects.create_user(username,email,password)
                user.save()

                tester1=form.save(commit=False)
                tester1.user=user
                tester1.save()
    context= {'form': form}
    return render(request, 'tester/tregister.html')    