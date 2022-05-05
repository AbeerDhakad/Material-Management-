from django.shortcuts import render
from django.http import JsonResponse
import uuid
import os
from.import Pool
def supplierInterface(request):
    return render(request,"SupplierInterface.Html")
def SupplierSubmit(request):
    try:
        suppliername = request.POST['suppliername']
        landlineno=request.POST['landlineno']
        mobileno=request.POST['mobileno']
        emailid=request.POST['emailid']
        address=request.POST['address']
        state=request.POST['state']
        city=request.POST['city']
        q = "insert into supplier(suppliername,landlineno,mobileno,emailid,address,state,city)values('{}',{},{},'{}','{}','{}','{}')".format(suppliername,landlineno,mobileno,emailid,address,state,city)
        print(q)
        db, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request, "supplierinterface.html", {'msg': 'Record successfully submitted '})

    except Exception as e:
        print(e)
        return render(request, "supplierinterface.html", {'msg': 'Fail to submit Record'})
def Displayallsupplier(request):
   try:
     db,cmd=Pool.ConnectionPool()
     q="select S.* from supplier S"
     cmd.execute(q)
     rows=cmd.fetchall()
     db.close()

     return render(request, "DisplayAllsupplier.html", {'rows':rows})

   except Exception as e:
      print("Error",e)
      return render(request, "DisplayAllsupplier.html", {'rows':[]})
def GetsupplierJSON(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from supplier"
        cmd.execute(q)
        rows=cmd.fetchall()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print('error',e)
        return JsonResponse([], safe=False)
def DisplayById(request):
    supplier=request.GET['supplierid']
    try:
        db, cmd = Pool.ConnectionPool()
        q="select S.* from supplier S where supplierid={}".format(supplier)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request, "EditCategoryById.html", {'row':row})
    except Exception as e:
        print(e)
        return render(request, "EditCategoryById.html", {'rows': []})
def EditDeletesupplier(request):
    btn=request.GET['btn']
    supplierid=request.GET['supplierid']
    print("xxxxxxxxxxxx",btn)
    if(btn=="Edit"):
     suppliername = request.GET['suppliername']
     try:
        db, cmd = Pool.ConnectionPool()
        q = "update supplier set suppliername='{}' where supplierid={}".format(suppliername,supplierid)
        print (q)
        cmd.execute(q)
        db.commit()
        db.close()
        return Displayallsupplier(request)
     except Exception as e:
        print("Error:", e)
        return Displayallsupplier(request)

    elif (btn=="Delete"):

        try:

            db, cmd = Pool.ConnectionPool()
            q = "delete from supplier where supplierd={}".format(supplierid)
            cmd.execute(q)
            db.commit()
            db.close()
            return Displayallsupplier(request)
        except Exception as e:
            print(e)
            return Displayallsupplier(request)
