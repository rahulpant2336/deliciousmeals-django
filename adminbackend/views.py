from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect

from django.contrib import messages
from .models import HomePageProject, HomeContactForm
from adminbackend.forms import HomeForm

# Create your views here.
def index(request):
    now = timezone.now()
    homepageprojects = HomePageProject.objects.filter(pub_date__year=now.year,
                                       pub_date__month=now.month,
                                       pub_date__day=now.day)[0:3]

    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            form = HomeForm()
            messages.success(request, 'Form submission successful.')
            return HttpResponseRedirect('/')
            #return HttpResponseRedirect('/thanks/')
        else:
            messages.error(request, 'Error in submission.')
            return HttpResponseRedirect('/')
    else:
        form = HomeForm()
    return render(request, 'adminbackend/index.html', {
      'homepageprojects' : homepageprojects,
      'form': form
    })
