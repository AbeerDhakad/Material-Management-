from django.shortcuts import render
import os
import uuid
from.import Pool

from django.http import JsonResponse
def CategoryView(request):
    return render(request,"SubCategory.Html")
def SubCategorySubmit(request):
    try:
        categoryid = request.POST['categoryid']
        subcategoryname=request.POST['subcategoryname']
        description=request.POST['description']
        picture = request.FILES['Icon']
        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]

        q = "insert into SubCategories(categoryid,subcategoryname,description,Icon)values({},'{}','{}','{}')".format(categoryid,subcategoryname,description ,filename)
        db, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        F = open("E:/MM/assets/" + filename, "wb")
        for chunk in picture.chunks():
            F.write(chunk)
        F.close()
        db.close()

        return render(request, "SubCategory.html", {'msg': 'Record successfully submitted '})
    except Exception as e:
        print(e)
        return render(request, "SubCategory.html", {'msg': 'Fail to submit Record'})
def DisplaySubCategories(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from subcategories"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,'DisplaySubcategory.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return render(request,'DisplaySubcategory.html', {'rows':[]})
def GetSubcategoryJSON(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from subcategories"
        cmd.execute(q)
        rows=cmd.fetchall()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print('error',e)
        return JsonResponse([], safe=False)
def DisplaySubcategoryById(request):
    subcategoryid=request.GET['subcategoryid']
    try:
        db, cmd = Pool.ConnectionPool()
        q = "select * from subcategories where subcategoryid={}".format(subcategoryid)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return render(request,'DisplaySubcategoryById.html', {'row': row})
    except Exception as e:
        print('error', e)
        return render(request,'DisplaySubcategoryById.html', {'row': []})

def EditDeleteSubategory(request):
    btn=request.GET['btn']
    subcategoryid=request.GET["subcategoryid"]
    print("xxxxxxxxxxxx",btn)
    if(btn=="Edit"):
        subcategoryname=request.GET['subcategoryname']
        scdescription=request.GET['description']
        try:
            db, cmd = Pool.ConnectionPool()
            q = "update subcategories set subcategoryname='{}' , description='{}' where subcategoryid={}".format(subcategoryname,scdescription,subcategoryid)
            print (q)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplaySubCategories(request)
        except Exception as e:
            print("Error:", e)
            return DisplaySubCategories(request)

    elif (btn=="Delete"):

        try:
            db, cmd = Pool.ConnectionPool()
            q = "delete from subcategories where subcategoryid={}".format(subcategoryid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplaySubCategories(request)
        except Exception as e:
            print(e)
            return DisplaySubCategories(request)

def EditSubategoryIcon(request):
    try:
        subcategoryid=request.GET['subcategoryid']
        subcategoryname=request.GET['subcategoryname']
        subcategoryicon=request.GET['icon']
        row=[subcategoryid,subcategoryname,subcategoryicon]
        return render(request,"EditSubcategoryIcon.html",{'row':row})
    except Exception as e:
        print('error:',e)
        return render(request,"EditSubcategoryIcon.html",{'row':[]})

def SaveEditSubcategoryIcon(request):
    try:
        subcategoryid=request.POST['subcategoryid']
        oldpicture=request.POST['oldicon']
        picture=request.FILES['icon']
        filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
        q="update subcategories set icon='{}' where subcategoryid={}".format(filename,subcategoryid)
        print(q)
        db,cmd=Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        F=open("E:/MM/assets/"+filename,"wb")
        for chunk in picture.chunks():
            F.write(chunk)
        F.close()
        db.close()
        os.remove('D:/MM/assets/'+oldpicture)
        return DisplaySubCategories(request)
    except Exception as e:
        print("Error:", e)
        return DisplaySubCategories(request)