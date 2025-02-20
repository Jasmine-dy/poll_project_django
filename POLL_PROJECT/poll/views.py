from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import poll

# Create your views here.

def home(request):
    polls = poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
     form = CreatePollForm()
    context = {
        'form': form
    }
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    pooll = poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            pooll.option_one_count += 1
        elif selected_option == 'option2':
            pooll.option_two_count += 1
        elif selected_option == 'option3':
            pooll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invaled form!')
        
        pooll.save()

        return redirect('results', poll_id)

    context = {
        'pooll' : pooll
    }
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    pooll = poll.objects.get(pk=poll_id)
    context = {
        'pooll' : pooll
    }
    return render(request, 'poll/results.html', context)
     