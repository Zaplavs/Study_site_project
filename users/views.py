from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import  login_required
from users.forms import UserLoginForm, UserRegistrationForm,UserProfileform
from django.urls import reverse
from products.models import Basket
# Create your views here.

def login(requets):
    if requets.method == 'POST':
        form = UserLoginForm(data=requets.POST)
        if form.is_valid():
            username = requets.POST['username']
            password = requets.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(requets,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(requets,'users/login.html', context=context)

def registration(requets):
    if requets.method == 'POST':
        form = UserRegistrationForm(data=requets.POST)
        if form.is_valid():
            form.save()
            messages.success(requets,"Поздравляю регистрация прошла успешна")
            return  HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(requets,'users/registration.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileform(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileform(instance=request.user)
    baskets = Basket.objects.filter(user = request.user)
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity =  sum(basket.quantity for basket in baskets)
    # for basket in baskets:
    #     total_sum = total_sum + basket.sum()
    #     total_quantity += basket.quantity
    context = {'title':'Store - Profile',
               'form': form,
               'baskets': Basket.objects.filter(user = request.user),
                'total_sum' :total_sum,
                "total_quantity" :total_quantity,
               }
    return  render(request, 'users/profile.html', context)

def logout(requets):
    auth.logout(requets)
    return HttpResponseRedirect(reverse('index'))

