from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.contrib.auth import authenticate, login, logout
from .filters import SponsorFilter
from django.db.models import Sum
from django.contrib import messages
from .pagination import CustomPagination

from main.models import (
    SponsorModel,
    StudentModel,
    UniversityModel,
    SponsorshipModel,
)
from .serializers import (
    SponsorSerializer,
    StudentSerializer,
    UniversitySerializer,
    SponsorshipSerializer,
    SponsorDetailSerializer,
    StudentDetailSerializer,
)
from rest_framework import (
    views,
    generics,

)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
)


#
# def loginView(self, request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == "POST":
#             username = request.method.POST.get('username')
#             password = request.method.POST.get('password')
#
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 messages.info(request, "Sizning Username yoki Parolingiz xato")


# def logoutView(request):
#     logout(request)
#     return redirect('login')
#     # No backend authenticated the credentials

class DashboardView(views.APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        all_payed_money = SponsorshipModel.objects.aggregate(Sum('money'))['money__sum']
        all_contract = StudentModel.objects.aggregate(Sum('contract'))['contract__sum']
        data = {
            'all_payed_money': all_payed_money,
            'all_contract': all_contract,
            'all_rest': all_contract - all_payed_money,
        }
        return Response(data=data)


class SponsorView(generics.ListCreateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('status', 'choice_money', 'updated_date')


class SponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorDetailSerializer


class UniversityView(generics.ListCreateAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class StudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    pagination_class = CustomPagination
    serializer_class = StudentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('student_type', 'university')


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentDetailSerializer



class SponsorshipView(generics.ListCreateAPIView):
    queryset = SponsorshipModel.objects.all()
    serializer_class = SponsorshipSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, IsAdminUser]


class SponsorshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SponsorshipModel.objects.all()
    serializer_class = SponsorshipSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# class StudentSponsor(views.APIView):
#     def get(self, request, pk):
#         # sponsor = SponsorModel.objects.get(id=pk)
#         # student = StudentModel.objects.get(id=pk)
#         sponsors = SponsorModel.objects.filter(sponsorships__student__id=pk)
#         students = StudentModel.objects.filter(studentships__sponsor__id=pk)
#         data = {
#             'sponsor_id': pk,
#             'students': students,
#             'student_id': pk,
#             'sponsors': sponsors,
#         }
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response( data=serializer.data)
    #     return Response(data=data)


