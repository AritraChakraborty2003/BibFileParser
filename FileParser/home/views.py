from django.shortcuts import render
from django.conf import settings
from pybtex.database.input import bibtex
from home.models import Data,DataUpdated
from django.http import HttpResponse
import urllib, urllib.request
import xmltodict
import pprint
import json
# Create your views here.
def index(request):
    if request.method=="POST":
        syear=request.POST.get("syear")
        eyear=request.POST.get("eyear")
        #query=request.POST.get("query")
        que=request.POST.get("query1")
        arr=que.split(',')
        query=arr[0]
        try:
            query1=arr[1]
        except:
            pass
        try:
         query2=arr[2]
        except:
           pass
        try:
            query3=arr[3]
        except:
           pass
        years=[]
        print(arr)
        if syear>eyear:
            return HttpResponse("This is a error")
        for i in range((int)(syear),(int)(eyear)+1):
            years.append(i)
        lst=[]
        for x in years:
        
           data=DataUpdated.objects.filter(year=x).values_list("title","year","abstract","url")
           for l in data:
            splt=l[2].split()
            splt1=l[0].split()
            #print(splt)
            if(len(arr)==1):
                if (query in splt or query in splt1):
                     
                 #print("Title:- ",l[0])
                 print("Year:- ",l[1])
                 #print("URL:- ",l[3])
                 #print("Abstract:- ",l[2])
               
                 lst.append(l)
              
            
            elif(len(arr)==2):
                if (query in splt or query in splt1) and (query1 in splt or query1 in splt1):
                 #print("Title:- ",l[0])
                 print("Year:- ",l[1])
                 #print("URL:- ",l[3])
                 #print("Abstract:- ",l[2])
               
                 lst.append(l)
               
            elif(len(arr)==3):
                if (query in splt or query in splt1) and (query1 in splt or query1 in splt1) and (query2 in splt or query2 in splt1):
                 #print("Title:- ",l[0])
                 print("Year:- ",l[1])
                 #print("URL:- ",l[3])
                 #print("Abstract:- ",l[2])
               
                 lst.append(l)
             
            else:
                if (query in splt or query in splt1) and (query1 in splt or query1 in splt1) and (query2 in splt or query2 in splt1) and (query3 in splt or query3 in splt1):
    
                 #print("Title:- ",l[0])
                 print("Year:- ",l[1])
                 #print("URL:- ",l[3])
                 #print("Abstract:- ",l[2])
               
                 lst.append(l)
        return render(request,"index.html",{"data":lst,"length":len(lst)}) 
       
    return render(request,"index.html")
      
        
    """#for x in years:
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
        return render(request,"index.html",{"data":lst,"length":len(lst)})"""
def aravix(request):
   mst=[]
   if request.method== "POST":
    
      key=request.POST.get("keyword")
      url = 'http://export.arxiv.org/api/query?search_query=all:'+key+'&start=0&max_results=10'
      data = urllib.request.urlopen(url)
      my_xml=data.read().decode('utf-8')
      my_dict=xmltodict.parse(my_xml)
      for i in range(7):
        lst=[]
        print("Summary: ",my_dict['feed']['entry'][i]['summary'])
        print("Title: ",my_dict['feed']['entry'][i]['title'])
        print("Link: ",my_dict['feed']['entry'][i]['id'])
        lst.append(my_dict['feed']['entry'][i]['summary'])
        lst.append(my_dict['feed']['entry'][i]['title'])
        lst.append(my_dict['feed']['entry'][i]['id'])
        mst.append(lst)
        
      return render(request,"arvix.html",{'length':len(mst),'data':mst})
   return render(request,"arvix.html")