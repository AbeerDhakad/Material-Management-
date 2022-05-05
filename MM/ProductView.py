from django.shortcuts import render
from django.http import JsonResponse
import uuid
import os
from.import Pool
def pView(request):
    return render(request,"ProductView.Html")
def ProductSubmit(request):
    try:
        categoryid = request.POST['categoryid']
        subcategoryid=request.POST['subcategoryid']
        productname=request.POST['productname']
        description=request.POST['pdescription']
        gst=request.POST['GST']
        picture = request.FILES['Icon']
        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]
        q = "insert into product(categoryid,subcategoryid,productname,description,icon)values({},{},'{}','{}','{}')".format(categoryid,subcategoryid,productname,description, filename)
        db, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        F = open("E:/MM/assets/" + filename, "wb")
        for chunk in picture.chunks():
            F.write(chunk)
        F.close()
        db.close()

        return render(request, "ProductView.html", {'msg': 'Record successfully submitted '})

    except Exception as e:
        print(e)
        return render(request, "ProductView.html", {'msg': 'Fail to submit Record'})

def GetProductJSON(request):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "select * from product"
            cmd.execute(q)
            rows = cmd.fetchall()
            return JsonResponse(rows, safe=False)
        except Exception as e:
            print('error', e)
            return JsonResponse([], safe=False)
def DisplayProducts(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q = "select P.*,(select C.categoryname from categories C where C.categoryid=P.categoryid),(select S.subcategoryname from subcategories S where S.subcategoryid=P.subcategoryid) from product P"

        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,'ProductDisplay.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return render(request,'ProductDisplay.html', {'rows':[]})
def DisplayById(request):
    product=request.GET['productid']
    try:
        db, cmd = Pool.ConnectionPool()
        q="select P.* from product P where productid={}".format(product)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request, "EditProductById.html", {'row':row})
    except Exception as e:
        print(e)
        return render(request, "EditProductById.html", {'rows': []})
def EditDeleteProduct(request):
    btn=request.GET['btn']
    productid=request.GET['productid']
    print("xxxxxxxxxxxx",btn)
    if(btn=="Edit"):
     productname = request.GET['productname']
     try:
        db, cmd = Pool.ConnectionPool()
        q = "update product set productname='{}' where productid={}".format(productname,productid)
        print (q)
        cmd.execute(q)
        db.commit()
        db.close()
        return DisplayProducts(request)
     except Exception as e:
        print("Error:", e)
        return DisplayProducts(request)

    elif (btn=="Delete"):

        try:

            db, cmd = Pool.ConnectionPool()
            q = "delete from product where productid={}".format(productid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayProducts(request)
        except Exception as e:
            print(e)
            return DisplayProducts(request)

def EditProductIcon(request):
    try:
        productid=request.GET['productid']
        productname=request.GET['productname']
        icon=request.GET['icon']
        row=[productid,productname,icon]
        return render(request,"EditProductIcon.html",{'row':row})
    except Exception as e:
        print('error:',e)
        return render(request,"EditProductIcon.html",{'row':[]})

def SaveEditProductIcon(request):
    try:
        productid=request.POST['productid']
        oldpicture=request.POST['oldicon']
        picture=request.FILES['icon']
        filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
        q="update product set icon = '{}' where productid={}".format(filename,productid)
        print(q)
        db,cmd=Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        F=open("E:/MM/assets/"+filename,"wb")
        for chunk in picture.chunks():
            F.write(chunk)
        F.close()
        db.close()
        os.remove('E:/MM/assets/'+oldpicture)
        return DisplayProducts(request)
    except Exception as e:
        print("Error:", e)
        return DisplayProducts(request)