from django.shortcuts import render



def index(req):
    x = {'name':'mahmoud','age':44}
    return render(req, 'app1/index.html',x)
def about(req):
    return render(req, 'app1/about.html')

# Create your views here.
