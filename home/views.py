from django.shortcuts import render
from django.conf import settings
from pybtex.database.input import bibtex
from home.models import Data,DataUpdated
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
        syear=request.POST.get("syear")
        query=request.POST.get("query")
        query1=request.POST.get("query1")
        """print(query)
        
        years=[]
        if syear>eyear:
            return HttpResponse("This is a error")
        for i in range((int)(syear),(int)(eyear)+1):
            years.append(i)"""
     
        
        #for x in years:
        lst=[]
        data=DataUpdated.objects.filter(year=syear).values_list("title","year","abstract","url")
        for l in data:
           splt=l[2].split()
           splt1=l[0].split()
           print(splt)
           if (query in splt or query in splt1) or (query1 in splt or query1 in splt1):
    
            #print("Title:- ",l[0])
            #print("Year:- ",l[1])
            #print("URL:- ",l[3])
            print("Abstract:- ",l[2])
            lst.append(l)
        return render(request,"index.html",{"data":lst,"length":len(lst)})
    return render(request,"index.html")