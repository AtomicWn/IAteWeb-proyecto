from django.shortcuts import render, redirect
from .forms import NewRegister

from django.shortcuts import get_object_or_404
from Home.models import Survey
from Home.forms import SurveyForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def IAteHome(request):
    return render(request, 'IAteHome.html')

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form = NewRegister()
    return render(request,'registration/register.html',{'form':NewRegister})

########################################################################################################
def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    post_data = request.POST if request.method == "POST" else None
    form = SurveyForm(survey, post_data)
    
    url = reverse("show-survey", args=(id,))
    if form.is_bound and form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Submissions saved.')
        return redirect(url)
    
    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "survey.html", context)