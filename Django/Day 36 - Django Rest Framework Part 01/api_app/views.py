from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_app.serializers import *
from api_app.models import *

@api_view(['GET','POST'])
def student(request):
  if request.method=='GET':
    student_data=StudentModel.objects.all()
    serializer_data=StudentSerializer(student_data,many=True)

    context={
      'success': True,
      'message': 'Student data get successful',
      'data':serializer_data.data,
    }
    return Response(context)

  elif request.method=='POST':
    serializer_data=StudentSerializer(data=request.data)
    if serializer_data.is_valid():
      serializer_data.save()
      context={
        'success': True,
        'message': 'Student Add successful',
        'data':serializer_data.data,
      }
      return Response(context)
    else:
      context={
        'success': False,
        'message': 'Student Add failed',
        'error':serializer_data.errors,
      }
      return Response(context)


@api_view(['GET','PATCH','DELETE'])
def student_details(request, id):
  try:
    student_data = StudentModel.objects.get(id = id)
  except:
    return Response({
          "success": False,
          "message": "Student Data not Found"
      })
  if request.method == 'GET':
    serializer_data = StudentSerializer(student_data)
    return Response({
        "success": True,
        "message": "Student Data Get Successfully",
        "data": serializer_data.data
    })

  elif request.method == 'PATCH':
    serializer_data = StudentSerializer(student_data, data=request.data)
    if serializer_data.is_valid():
      serializer_data.save()
      return Response({
          "success": True,
          "message": "Student Updated successfully",
          "data": serializer_data.data
      })
  elif request.method == 'DELETE':
    student_data.delete()
    return Response({
        "success": True,
        "message": "Student Deleted successfully",
        "data": []
    })
