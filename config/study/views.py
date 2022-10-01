from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# HelloView로 요청이 오면
def HelloView(request):

    print(request.__dict__)

    data = {
        'text': 'test'
    }

    return render(request, 'study/index.html', data)
