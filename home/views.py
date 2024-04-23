from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

@login_required
def gallery(request):
    return render(request, 'home/gallery.html')

@login_required
def contact(request):
    return render(request, 'home/contact.html')
