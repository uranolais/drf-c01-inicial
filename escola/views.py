from django.http import JsonResponse

def estudantes(request): #pode ser qualquer palavra chave, mas por padrão utilizamos em ingles 'request'
    if request.method == 'GET':
        estudante = {
            'id':1,
            'nome': 'Lais'
            }
        return JsonResponse(estudante)