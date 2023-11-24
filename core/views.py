from django.http import HttpResponse

from core.tasks import debug_task


def home(request):
    debug_task.delay()
    return HttpResponse("Olá")
