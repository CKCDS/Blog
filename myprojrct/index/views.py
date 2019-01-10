from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index_views(request):
    return render(request,"index.html")
# 处理登入状业务
# def login_views(request):
#     if request.method == "GET":
#         url = request.META.get('HTTP_REFERER', "/")
#         if request.session.get("uphone"):
#             return redirect(url)
#         elif request.COOKIES.get("uphone"):
#             request.session["uphone"] = request.COOKIES.get("uphone")
#             url = request.META.HTTP_REFERER
#             return redirect(url)
#         else:
#             forms = LoginFrom()
#             resp = render(request, "login.html", locals())
#             resp.set_cookie("url", url, 60 * 60 * 24)
#             return resp
#     # post请求  登入请求
#     else:
#         uphone = request.POST.get("uphone")
#         upwd = request.POST.get("upwd")
#         isSave = request.POST.get("isSave")
#         try:
#             user = User.objects.get(uphone=uphone, upwd=upwd)
#         except:
#             user = None
#         if user:
#             # 登入成功
#             url = request.COOKIES.get("url")
#             request.session["uphone"] = uphone
#             resp = render(request, url)
#             resp.delete_cookie("url")
#             # 如果记住密码则将数据保存进cookies
#             if isSave:
#                 resp.set_cookie("uphone", user.id, 60 * 60 * 24 * 31 * 12)
#             return resp
#         else:
#             return redirect("/login/")