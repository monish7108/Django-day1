from django.shortcuts import render

def index(request):
    return render(request, "personal/home.html")

def contact(request):
    return render(request, 'personal/basic.html',{'content':['hello','Why the hell is this printing','If you would like to contact me, please email me.','monish.lalchandani@tarams.com']})
