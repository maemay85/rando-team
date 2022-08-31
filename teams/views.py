from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Team, Member
from .forms import NameForm

# Create your views here.

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def your_name(request):
    template = loader.get_template('your_name.html')
    return HttpResponse(template.render({}, request))

def thanks(request):
    return render(request, 'thanks.html')
