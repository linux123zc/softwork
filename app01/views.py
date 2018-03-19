from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.

def index(request):
    return render(request,'index.html')



def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.User.objects.filter(username=u, password=p).first()
        # count = models.UserInfo.objects.filter(username=u,password=p).count()
        if obj:
            return redirect('/index/')
        else:
            return render(request, 'login.html')

    else:
        return redirect('/index/')

def register(request):
    import json
    error_msg = ""
    try:
        u = request.POST.get('username')
        p1 = request.POST.get('password')
        p2 = request.POST.get('password2')

        if u:
            if p1 == p2:
                models.User.objects.create(
                    username = u,
                    password = p1,
                )
                error_msg = "注册成功"
                return redirect('/login/')
            else:
                error_msg = "信息错误"
        else:
                error_msg = "信息错误"

    except Exception as e:
        error_msg = "请求错误"
    return render(request,'register.html',{'error_msg':error_msg})