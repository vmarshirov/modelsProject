import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Abc
from .forms import CreateAbcForm


def index(request):
    return render(request, 'main/index.html')


# def index(request):
#     name_main="index"
#     redirect_url=reverse ('index', args=(name_main))
#     return render(request, redirect_url)


def form_create(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            form.save()
            print("\nform:\n", form)
            return redirect('main:result')
    else:
        print("else:\n")
        form = CreateAbcForm()
    print('\nform:\n', form)

    context = {
        'form': form
    }
    print("\ncontext:\n", context)
    return render(request, 'main/form_create.html', context)


def result(request):
    # rows = Abc.objects.values_list()
    rows = Abc.objects.values_list()
    for row in rows:
        print ("\n row: ", row)
        last_data = [row[2], row[3], row[4]]
        if last_data[0] + last_data[1] == last_data[2]:
            result = " С равна сумме A и B"
        else:
            result = "С не равна сумме A и B"
        last_data.append(result)
        task_main = list()
        task_main.append(row[1])
        print('task_main:', task_main, 'last_data: ', last_data)
    context = {'task_main': task_main, 'last_data': last_data}
    return render(request, 'main/result.html', context)


def table(request):
    rows = Abc.objects.values_list()
    context = {'rows': rows}
    return render(request, 'main/table.html', context)


def list_main(request):
    list_main = (1, 2, 3, 4, 5)
    print(list_main)
    dict_main = {'x': 1, 'y': 2}
    print(dict_main)
    context = {'list_main': list_main, 'dict_main': dict_main}  # будем передавать в шаблон как один общий объект
    return render(request, 'main/list_main.html', context)


def datetime_nov(request):
    now = list()
    now.append(datetime.datetime.now())
    print('datetime.datetime.now(): ', now)
    list_main = now
    print(list_main)
    context = {'list_main': list_main}
    return render(request, 'main/datetime_now.html', context)
