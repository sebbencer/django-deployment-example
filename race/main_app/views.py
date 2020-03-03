from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
from main_app.forms import NewRunnerForm,ConsultForm
from main_app.models import Runner


def index(request):
    return render(request,'main_app/index.html')

def about_view(request):
    return render(request,'main_app/about.html')

def register_view(request):
    form = NewRunnerForm()
    if request.method == "POST":
        print('holi')
        form = NewRunnerForm(request.POST)

        if form.is_valid():
            runner = form.save(commit=False)
            ###AGREGAR NUMERO DE CORREDOR
            runner.number=1000
            runner.save()
        else:
            print('ERROR')
    form = NewRunnerForm()
    return render(request,'main_app/register.html',{'form':form})

def results_view(request):
    form = ConsultForm()
    runner_dict = {'runner_data':''}
    runner=''
    if request.method == "POST":
        form = ConsultForm(request.POST)

        if form.is_valid():
            number=form.cleaned_data['number']
            try:
                runner=Runner.objects.get(number=number)
                runner_dict = {'runner_data':runner}

            except Exception as e:
                pass

        else:
            print('ERROR')
    #return render(request,'main_app/results.html',{'form':form})
    return render(request,'main_app/results.html',context={'form':form,'runner_data':runner})

def route_view(request):
    return render(request,'main_app/route.html')
