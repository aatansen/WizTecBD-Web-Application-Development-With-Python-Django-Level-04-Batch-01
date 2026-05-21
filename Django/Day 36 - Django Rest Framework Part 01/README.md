# Context

- [Context](#context)
  - [CRUD using Function based `api_view`](#crud-using-function-based-api_view)
    - [Initial Setup](#initial-setup)
    - [Serializers](#serializers)
    - [API Endpoints](#api-endpoints)
    - [API Client Setup](#api-client-setup)
    - [Improve The Response](#improve-the-response)
    - [POST Request](#post-request)
    - [Individual Data View, Update, Delete](#individual-data-view-update-delete)

## CRUD using Function based `api_view`

### Initial Setup

- Create project `api_project`
- Create app `api_app`
- Add app name in `INSTALLED_APPS`
- Create a model `StudentModel` in [models.py](./api_app/models.py)

  ```py
  class StudentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    department = models.CharField(max_length=100, null=True)

    def __str__(self):
      return f'{self.name}'
  ```

- Register in [admin.py](./api_app/admin.py)
- Run database migrations command
- Create Superuser
- Add data in `StudentModel` from admin page

---
[⬆️ Go to Context](#context)

### Serializers

- To create serializer we have to install [djangorestframework](https://pypi.org/project/djangorestframework/)

  ```sh
  pip install djangorestframework
  ```

- Add this in `INSTALLED_APPS` in [settings.py](./api_project/settings.py)

  ```py
  INSTALLED_APPS = [
      ...
      # drf
      'rest_framework',
      # my apps
      'api_app',
  ]
  ```

- Now we will create [serializers.py](./api_app/serializers.py) in app directory

  ```py
  from rest_framework import serializers
  from api_app.models import *

  class StudentSerializer(serializers.ModelSerializer):
    class Meta:
      model=StudentModel
      fields='__all__'
  ```

---
[⬆️ Go to Context](#context)

### API Endpoints

- Now that we have serializer we can create endpoint in [views.py](./api_app/views.py)

  - Function based `api_view`

    ```py
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from api_app.serializers import *
    from api_app.models import *

    @api_view(['GET'])
    def student_list(request):
      if request.method=='GET':
        student_data=StudentModel.objects.all()
        serializer_data=StudentSerializer(student_data,many=True)

        context={
          'data':serializer_data.data,
        }
        return Response(context)
    ```

- Setup URL

---
[⬆️ Go to Context](#context)

### API Client Setup

- We can use [Postman](https://www.postman.com/) or VsCode Extension [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)

- Create new request
- Select `GET`
- Send Request to this route `http://127.0.0.1:8000/student-list/`
- If successful it will show the data from the database

---
[⬆️ Go to Context](#context)

### Improve The Response

  ```py
  @api_view(['GET'])
  def student_list(request):
    if request.method=='GET':
      student_data=StudentModel.objects.all()
      serializer_data=StudentSerializer(student_data,many=True)

      context={
        'success': True,
        'message': 'Student data get successful',
        'data':serializer_data.data,
      }
      return Response(context)
  ```

---
[⬆️ Go to Context](#context)

### POST Request

- We can either make different function

  ```py
  @api_view(['POST'])
  def student_add(request):
    if request.method=='POST':
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
  ```

- Or just add it in single function

  ```py
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
  ```

---
[⬆️ Go to Context](#context)

### Individual Data View, Update, Delete

  ```py
  @api_view(['GET','PATCH','DELETE'])
  def student_detail(request, pk):
    try:
      student_data = StudentModel.objects.get(id = pk)
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
  ```

---
[⬆️ Go to Context](#context)
