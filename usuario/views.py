from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import userForm, datosForm
from django.contrib.auth.models import User
from .registers import guardarUser

class Index(View):
    def get(self, request):
        template = 'index.html'
        form = userForm()
        formextra = datosForm()
        context = {
            'form': form,
            'extra': formextra
        }
        return render(request, template, context)

    def post(self, request):
        try:
            guardarUser(request.POST)
        except Exception as e:
            print(e)
            print(type(e))
                
        #form = userForm(request.POST)

        #username = request.POST.get('nombre')
        #password = request.POST.get('contra')
        #email = request.POST.get('email')
        #if form.is_valid():
            #user = User.objects.create_user(username=username, password=password, email=email)
            #user.save()
            #form.save()
        #else:
            #print('no chavo')

        return redirect('user:index')
