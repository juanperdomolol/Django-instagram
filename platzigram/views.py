from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    return HttpResponse('Hello, world!')

def hola(request):
    return HttpResponse('no se parce')


def probando(request):    
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, la hora es {now}'.format(now=str(now)))

def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )
def hi(request, name, age):
    if age < 12:
        message ='sorry {}, yoy are not allowed here'.format(name)
    else:
        message = 'Hello,{}! Welcome to platigram'.format(name)

    return HttpResponse(message)