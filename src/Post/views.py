from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Home Page'
    pagename = 'Home Page'
    return render(request, 'home.html', {'title':title, 'pagename':pagename})

def projects(request):
    title = 'My Projects'
    pagename = 'My Projects'
    return render(request, 'projects.html', {'title':title, 'pagename':pagename})