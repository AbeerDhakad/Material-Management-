from django.shortcuts import render
from django.http import JsonResponse
import uuid
import os
from.import Pool
def CategoryView(request):
    return render(request,"Category.Html")
def CategorySubmit(request):
    try:
        categoryname = request.POST['categoryname']
        picture = request.FILES['Icon']
        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]
        q = "insert into categories(Categoryname,icon)values('{}','{}')".format(categoryname,filename)
        print(q)
        db, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        F = open("E:/MM/assets/" + filename, "wb")
        for chunk in picture.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, "Category.html", {'msg': 'Record successfully submitted '})

    except Exception as e:
        print(e)
        return render(request, "Category.html", {'msg': 'Fail to submit Record'})
def DisplayallCategory(request):
   try:
     db,cmd=Pool.ConnectionPool()
     q="select C.* from categories C"
     cmd.execute(q)
     rows=cmd.fetchall()
     db.close()

     return render(request, "DisplayAllCategory.html", {'rows':rows})

   except Exception as e:
      print("Error",e)
      return render(request, "DisplayAllCategory.html", {'rows':[]})

def GetCategoryJSON(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print('error',e)
        return JsonResponse([], safe=False)


def DisplayById(request):
    category=request.GET['categoryid']
    try:
        db, cmd = Pool.ConnectionPool()
        q="select C.* from categories C where categoryid={}".format(category)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request, "EditCategoryById.html", {'row':row})
    except Exception as e:
        print(e)
        return render(request, "EditCategoryById.html", {'rows': []})
def EditDeleteCategory(request):
    btn=request.GET['btn']
    categoryid=request.GET['categoryid']
    print("xxxxxxxxxxxx",btn)
    if(btn=="Edit"):
     categoryname = request.GET['categoryname']
     try:
        db, cmd = Pool.ConnectionPool()
        q = "update categories set categoryname='{}' where categoryid={}".format(categoryname,categoryid)
        print (q)
        cmd.execute(q)
        db.commit()
        db.close()
        return DisplayallCategory(request)
     except Exception as e:
        print("Error:", e)
        return DisplayallCategory(request)

    elif (btn=="Delete"):

        try:

            db, cmd = Pool.ConnectionPool()
            q = "delete from categories where categoryid={}".format(categoryid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayallCategory(request)
        except Exception as e:
            print(e)
            return DisplayallCategory(request)
def EditCategoryIcon(request):
    try:
        categoryid=request.GET['categoryid']
        categoryname=request.GET['categoryname']
        categoryicon=request.GET['categoryicon']
        row=[categoryid,categoryname,categoryicon]
        return render(request,"EditCategoryIcon.html",{'row':row})
    except Exception as e:
        print('error:',e)
        return render(request,"EditCategoryIcon.html",{'row':[]})

def SaveEditCategoryIcon(request):
    try:
        categoryid=request.POST['categoryid']
        oldpicture=request.POST['oldicon']
        picture=request.FILES['categoryicon']
        filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
        q="update categories set icon = '{}' where categoryid={}".format(filename,categoryid)
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
        return DisplayallCategory(request)
    except Exception as e:
        print("Error:", e)
        return DisplayallCategory(request)