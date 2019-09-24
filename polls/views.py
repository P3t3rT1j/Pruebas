# Create your views here.


from django.http import  HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    # return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse('Hola Mundo!. polls index')

#def detail(request, question_id):
    #   question = get_object_or_404(Question, pk=question_id)
    #  return render(request, 'polls/detail.html', {'question': question})

#def results(request, question_id):
    # response = "esta viendo la respuesta de la pregunta %s."
    # return HttpResponse(response % question_id)
    #   question = get_object_or_404(Question, pk=question_id)
    #  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("esta votando en la pregunta %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




# vistas genericas
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
    
    
    

def requestAjax(request):
    data={
            'es_valido':False,
        }
    
    if request.is_ajax():
        messsage = request.POST.get('message')
        
        if messsage=='Quiero ajax response':
            data.update(es_valido=True)
            data.update(response='Esta es la respuesta esperada')
            
    return JsonResponse(data)


def obtenerRespuestas(request):
    
    data={
            'es_valido':True,
        }
    
    if request.is_ajax():
        question_id=request.GET.get("question_id")
    
        question = get_object_or_404(Choice, pk=question_id)
        #question= 
        
        print(question)
    data={
            'es_valido':True,
            'respuestas':'Recupero respuestas',
        }
    
    return JsonResponse(data);

        
