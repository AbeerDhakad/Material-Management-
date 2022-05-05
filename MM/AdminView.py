from django.shortcuts import render
from . import  PoolDict

def AdminLogout(request):
  del request.session['ADMIN']
  return render(request,"AdminLogin.Html")

def AdminView(request):
    return render(request,"AdminLogin.Html")
def checkAdminLogin(request):
  try:
    emailid=request.POST['emailid']
    password = request.POST['password']

    db, cmd = PoolDict.ConnectionPool()
    q="select * from admin where emailid='{}' and password='{}'".format(emailid,password)
    cmd.execute(q)
    result=cmd.fetchone()
    print(result)
    if (result):
        request.session['ADMIN'] = result
        return render(request, "AdminDashBoard.html", {'result': result})
    else:
       return render(request, "AdminLogin.html", {'result': result,'msg':'invalid emailid or password'})
    db.close()
  except Exception as e:
    print("Error",e)
    return render(request, "AdminLogin.html", {'result': {},'msg':'Server Error'})