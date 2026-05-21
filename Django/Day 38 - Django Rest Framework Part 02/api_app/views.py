from rest_framework.views import APIView
from api_app.models import *
from api_app.serializers import *
from rest_framework.response import Response

# GET, POST
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
