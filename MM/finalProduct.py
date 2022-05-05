from django.shortcuts import render
from django.http import JsonResponse
from . import  Pool
import uuid
import os
from.import PoolDict
import random
def ProdcutInterface(request):
    return render(request,"FinalProductView.html")
def FinalProductInterface(request):
    try:
        result = request.session['ADMIN']
        return render(request, "FinalProductInterface.html")
    except Exception as e:
        return render(request, 'AdminLogin.html')

def DisplayFinalProductByIdJSON(request):
    finalproductid = request.GET['finalproductid']
    try:
        dbe, cmd = PoolDict.ConnectionPool()
        q = "select FP.*,(select C.categoryname from categories C where C.categoryid = FP.categoryid),(select S.subcategoryname from subcategories S where S.subcategoryid = FP.subcategoryid), (select P.productname from product P where P.productid = FP.productid) from finalproduct FP where finalproductid = {}".format(finalproductid)
        cmd.execute(q)
        row = cmd.fetchone()
        dbe.close()
        return JsonResponse(row, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False)

def DisplayUpdatedStock(request):
    return render(request, "ListProductEmployee.html")

def DisplayUpdatedStockdate(request):
    return render(request, "ListDateProductEmployee.html")
def DisplayFinalProductAllJSON(request):
    pattern = request.GET['pattern']
    try:
        dbe, cmd = PoolDict.ConnectionPool()
        q = "select FP.*,(select C.categoryname from categories C where C.categoryid = FP.categoryid),(select S.subcategoryname from subcategories S where S.subcategoryid = FP.subcategoryid), (select P.productname from product P where P.productid = FP.productid) from finalproduct FP where finalproductname like '%{}%'".format(pattern)
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False)
def DisplayFinalProductAllDateJSON(request):
    pattern = request.GET['fdate']
    pattern1=request.GET['tdate']
    try:
        dbe, cmd = PoolDict.ConnectionPool()
        q = "select finalproduct as FP.*,(select C.categoryname from categories C where C.categoryid = FP.categoryid),(select S.subcategoryname from subcategories S where S.subcategoryid = FP.subcategoryid), (select P.productname from product P where P.productid = FP.productid) from purchase P where dateofpurchase like '%{}%' and '%{}%'".format(pattern,pattern1)
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False)

def finalproductsubmit(request):
    try:
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        productid = request.POST['productid']
        productname=request.POST['productname']
        size=request.POST['size']
        weight=request.POST['weight']
        stock=request.POST['Stock']
        price=request.POST['price']
        picture = request.FILES['icon']
        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]
        q = "insert into finalproduct(categoryid,subcategoryid,productid,finalproductname,size,weight,stock,price,icon)values({},{},{},'{}','{}','{}',{},{},'{}')".format(categoryid,subcategoryid,productid,productname,size,weight,stock,price,filename)
        print(q)
        db, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        F = open("E:/MM/assets/" + filename, "wb")
        for chunk in picture.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, "finalproductView.html", {'msg': 'Record successfully submitted '})

    except Exception as e:
        print(e)
        return render(request, "finalproductView.html", {'msg': 'Fail to submit Record'})
def GetfinalProductJSON(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from finalproduct"
        cmd.execute(q)
        rows=cmd.fetchall()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print('error',e)
        return JsonResponse([], safe=False)

def DisplayallProduct(request):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "select F.* from finalproduct F"
            cmd.execute(q)
            rows = cmd.fetchall()
            db.close()

            return render(request, "DisplayfinalProduct.html", {'rows': rows})

        except Exception as e:
            print("Error", e)
            return render(request, "DisplayfinalProduct.html", {'rows': []})

def DisplayFinalProductEmployee(request):
    try:
        dbe, cmd = Pool.ConnectionPool()
        q = "select FP.*,(select C.categoryname from categories C where C.categoryid = FP.categoryid),(select S.subcategoryname from subcategory S where S.subcategoryid = FP.subcategoryid), (select P.productname from products P where P.productid = FP.productid) from finalproducts FP"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return render(request, "DisplayFinalProductEmployee.html", {'rows': rows})
    except Exception as e:
        print(e)
        return render(request, "DisplayFinalProductEmployee.html", {'rows': []})
