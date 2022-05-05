from django.shortcuts import render
from . import Pool


def PurchaseInterface(request):
    try:
        result = request.session['EMPLOYEE']
        return render(request, "PurchaseInterface.html",{'result':result})
    except Exception as e:
        return render(request, 'EmployeeLogin.html')

def PurchaseSubmit(request):
    try:
        employeeid = request.POST['employeeid']
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        productid = request.POST['productid']
        finalproductid = request.POST['finalproductid']
        datepurchase = request.POST['datepurchase']
        supplierid = request.POST['supplierid']
        stock = request.POST['stock']
        amount = request.POST['amount']

        q = "insert into purchase (employeeid, categoryid, subcategoryid, productid, finalproductid, dateOFpurchase, supplierid, stock, amount) values ({}, {}, {}, {}, {}, '{}', {}, {}, {} )".format(
            employeeid, categoryid, subcategoryid, productid, finalproductid, datepurchase, supplierid, stock, amount)
        print(q)
        dbe, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        #Update Stock

        q="update finalproduct set price=((price+{})/2) , stock=stock+{} where finalproductid={}".format(amount,stock,finalproductid)
        cmd.execute(q)


        dbe.commit()
        dbe.close()
        return render(request, "PurchaseInterface.html", {'msg': 'Record Successfully Submitted'})
    except Exception as e:
        print("Error :", e)
        return render(request, "PurchaseInterface.html", {'msg': 'Fail to Submit Record'})


def DisplayAllPurchase(request):
    try:
        dbe, cmd = Pool.ConnectionPool()
        q = "select PP.*,(select C.categoryname from categories C where C.categoryid = PP.categoryid),(select S.subcategoryname from subcategories S where S.subcategoryid = PP.subcategoryid), (select P.productname from product P where P.productid = PP.productid), (select FP.finalproductname from finalproduct FP where FP.finalproductid = PP.finalproductid), (select S.suppliername from supplier S where S.supplierid = PP.supplierid) from purchase PP"
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return render(request, "DisplayAllPurchaseProduct.html", {'rows': rows})
    except Exception as e:
        print(e)
        return render(request, "DisplayAllPurchaseProduct.html", {'rows': []})


def EditDeletePurchasetRecord(request):
    btn = request.GET['btn']
    transactionid = request.GET['transactionid']
    if(btn == "Edit"):
        employeeid = request.GET['employeeid']
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        productid = request.GET['productid']
        finalproductid = request.GET['finalproductid']
        datepurchase = request.GET['datepurchase']
        supplierid = request.GET['supplierid']
        stock = request.GET['stock']
        amount = request.GET['amount']
        try:
            dbe, cmd = Pool.ConnectionPool()
            q = "update purchase set employeeid = {}, categoryid = {}, subcategoryid = {}, productid = {}, finalproductid = {}, datepurchase = '{}', supplierid = {}, stock = {}, amount = {} where transactionid={}".format(
                employeeid, categoryid, subcategoryid, productid, finalproductid, datepurchase, supplierid, stock, amount, transactionid)
            print(q)
            cmd.execute(q)
            dbe.commit()
            row = cmd.fetchone()
            dbe.close()
            return DisplayAllPurchase(request)
        except Exception as e:
            print(e)
            return DisplayAllPurchase(request)

    elif(btn == "Delete"):
        try:
            dbe, cmd = Pool.ConnectionPool()
            q = "delete from purchase where transactionid={}".format(
                transactionid)
            cmd.execute(q)
            dbe.commit()
            row = cmd.fetchone()
            dbe.close()
            return DisplayAllPurchase(request)
        except Exception as e:
            print(e)
            return DisplayAllPurchase(request)
