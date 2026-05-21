# Context

- [Context](#context)
  - [CRUD using Class based `APIView`](#crud-using-class-based-apiview)
    - [Initial Setup](#initial-setup)
    - [Serializers](#serializers)
    - [API Endpoints](#api-endpoints)
    - [API Client Setup](#api-client-setup)

## CRUD using Class based `APIView`

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

- Now that we have `serializer` we can create endpoint in [views.py](./api_app/views.py)

  - Class based `APIView` for `GET` and `POST`

    ```py
    # get, post
    class student_api(APIView):
        def get(self, request):
            student_data = StudentModel.objects.all()
            serializer = StudentSerializer(student_data, many=True)
            return Response({
                "success": True,
                "message": "Data reterived Successfully.",
                "data": serializer.data
            })

        def post(self, request):
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Data created Successfully.",
                    "data": serializer.data
                })
            return Response({
                "success": False,
                "error": serializer.data
            })
    ```

  - Individual data `GET`, `PUT`, `PATCH`, `DELETE`

    ```py
    # single data GET, PUT, PATCH, DELETE
    class student_detail_api(APIView):
        def get_data(self, id):
            try:
                student = StudentModel.objects.get(id=id)
                return student
            except:
                return Response({
                    "success": False,
                    "message": "Data not found."
                })

        def get(self, request, pk):
            student = self.get_data(pk)
            serializer = StudentSerializer(student)
            return Response({
                "success": True,
                "message": "Data get Successfully.",
                "data": serializer.data
            })

        def put(self, request, pk):
            student = self.get_data(pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Data updated Successfully.",
                    "data": serializer.data
                })

        def patch(self, request, pk):
            student = self.get_data(pk)
            serializer = StudentSerializer(
                student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Data updated Successfully.",
                    "data": serializer.data
                })
            return Response({
                "success": True,
                "error": serializer.error
            })

        def delete(self, request, pk):
            self.get_data(pk).delete()
            return Response({
                "success": True,
                "message": "Data deleted Successfully."
            })
    ```

- Setup URL

> [!IMPORTANT]
>
> - When we create class based views we have to write URL pattern class name like this : `class_name.as_view()`

---
[⬆️ Go to Context](#context)

### API Client Setup

- We can use [Postman](https://www.postman.com/) or `VsCode` Extension [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)

- Create new request
- Select request type
- Send Request to this route `http://127.0.0.1:8000/student-api/`
- If successful it will show,edit,delete the data from the database

---
[⬆️ Go to Context](#context)
