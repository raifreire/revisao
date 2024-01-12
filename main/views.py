from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Aluno

def alunoView(request):
    alunos_list = Aluno.objects.all
    #return HttpResponse('exibindo os alunos, sem mostrar nada')
    return render(request, 'main/alunos.html',{'alunos_list':alunos_list})
