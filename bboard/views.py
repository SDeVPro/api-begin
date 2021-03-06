from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb,Rubric
from django.template import loader
from bboard.models import Bb, Rubric
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BbForm

class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context 
        


# Create your views here.
# def index(request):
#     template = loader.get_template('index.html')
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs':bbs}
#     return HttpResponse(template.render(context,request))

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs,'rubrics':rubrics}
    return render(request,'index.html',context)

def by_rubric(request,rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs,'rubrics':rubrics,'current_rubric':current_rubric}
    return render(request,'by_rubric.html',context)