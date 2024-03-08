from django.shortcuts import render
from movies.models import Movie
from movies.forms import Movieform
# Create your views here.
def home(request):
    m=Movie.objects.all()
    return render(request,'home.html',{'m':m})

def moviedetails(request,s):
    m1=Movie.objects.get(id=s)
    return render(request,'moviedetails.html',{'m1':m1})

def addmovie(request):
    if(request.method=="POST"):
        form=Movieform(request.POST,request.FILES)
        if form.is_valid():
            form.save()  #saves the form object inside db table
        return home(request)
    form=Movieform() #empty form object
    return render(request,'addmovie.html',{'form':form})

def editmovie(request,p):
    m = Movie.objects.get(id=p)
    if (request.method == "POST"):
        form = Movieform(request.POST, request.FILES,instance=m)
        if form.is_valid():
            form.save()  # saves the form object inside db table
        return home(request)
    form=Movieform(instance=m)
    return render(request,'editmovie.html',{'form':form})

def deletemovie(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return home(request)