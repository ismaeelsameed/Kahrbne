# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from forms import PhotovoltaicForm


def home(request, template_name='base.html'):
    return render_to_response(template_name, {}, context_instance=RequestContext(request))


def photovoltaic(request, template_name='photovoltaic.html'):
    if request.method == 'GET':
        form = PhotovoltaicForm()
    else:
        # A POST request: Handle Form Upload
        form = PhotovoltaicForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            first_number = form.cleaned_data['first_num']
            second_number = form.cleaned_data['second_num']
            third_number = form.cleaned_data['third_num']
            result = int(first_number) + int(second_number) + int(third_number)
            form = PhotovoltaicForm()
            return render_to_response(template_name, {'form': form, 'result': result},
                                      context_instance=RequestContext(request))
    return render(request, template_name, {
        'form': form,
    })