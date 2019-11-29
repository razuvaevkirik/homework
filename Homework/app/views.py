from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View,ListView
from app.forms import *
from .models import *
from app.registration import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate


def main(request):
    computers = Computer.objects.all()
    return render(request, 'main.html', {"computers": computers})


def order_non_auth(request):
    return render(request, 'order_non_auth.html')


def registration(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            # ...
            return HttpResponseRedirect('/computers')
    return render(request, 'registration.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def authorization(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = "Пользователь не найден"
    return render(request, 'auth.html', locals())


def loginn(request):
    return render(request, 'user.html', locals())


def order_add(request):
    form = OrderForm(request.POST or None, request.FILES or None)
    computers = Computer.objects.all()
    if form.is_valid():
        instance = form.save()
        Order.objects.get(id_order=instance.pk).id_user.add(request.user.id)
        return HttpResponseRedirect(reverse('computers_url'))
    return render(request, "order_add.html", {"computers": computers, "form": form})


class ComputersList(ListView):
    model = Computer
    template_name = "computers.html"
    paginate_by = 3
    form_class = ComputerAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['computers'] = Computer.objects.all()
        return context

    def computer_add_modal(self, request):
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('computer_url', args=(instance.pk,)))
        return render(request, self.template_name, {'form': form})


def computer(request, computer_id=0):
    if request.method == 'POST':
        Computer.objects.get(id_computer=computer_id)
    return render(request, "computer.html", {'computer': Computer.objects.get(id_computer=computer_id)}, locals())


class OrdersView(ListView):
    model = Order
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(Order.objects.all().first().get_users)
        return context


def computer_add(request):
    form = ComputerAddForm(request.POST or None, request.FILES or None)
    context = {"form": form}
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect(reverse('computer_url', args=(instance.pk, )))
    return render(request, "computer_add.html", context)