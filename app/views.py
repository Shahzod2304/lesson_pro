from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')


def Contact(request):
    return render(request, 'contact.html')


def Trainer(request):
    return render(request, 'trainer.html')


def Why(request):
    return render(request, 'why.html')