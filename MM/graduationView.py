from django.http import JsonResponse
from . import Pool
def FetchALLgraduation(request):
 try:
     db,cmd=Pool.ConnectionPool()
     q="select * from graduation"
     cmd.execute(q)
     rows=cmd.fetchall()
     db.close()
     return JsonResponse(rows,safe=False)
 except Exception as e:
     print(e)
     return JsonResponse([], safe=False)

def FetchALLcourse(request):
 try:
     db,cmd=Pool.ConnectionPool()
     courseid=request.GET['courseid']
     q="select * from course where course ={}".format(courseid)
     cmd.execute(q)
     rows=cmd.fetchall()
     db.close()
     return JsonResponse(rows,safe=False)
 except Exception as e:
     print(e)
     return JsonResponse([], safe=False)