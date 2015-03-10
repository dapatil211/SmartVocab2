from django.shortcuts import render

def index(request):
    if(request.method == 'GET'):
        context = {'message': 'Hello World!'}
        return render(request, 'smartvocab/test.html', context)
    else:
        print request

# Create your views here.
