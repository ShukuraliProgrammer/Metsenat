from main.models import (
    SponsorModel,
    StudentModel,
    UniversityModel,
    SponsorshipModel,
)
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.db.models.functions import Coalesce
from django.db.models import Sum
from rest_framework.validators import ValidationError


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = (
            'id',
            'person_type',
            'first_name',
            'last_name',
            'father_name',
            'sponsor_number',
            'enter_money',
            'choice_money',
            'company_name',
        )

    def validate(self, value):
        if value['person_type'] == 'physical':
            value['company_name'] = None
        return value


class SponsorDetailSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    sponsorships = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = SponsorModel
        fields = (
            'id',

            'first_name',
            'last_name',
            'father_name',
            'sponsor_number',
            'pay_type',
            'enter_money',
            'choice_money',
            'sponsorships',
            'students',
        )

    def validate(self, value):
        if value['choice_money']:
            value['enter_money'] = None
        return value

    def get_students(self, sponsor):
        students = StudentModel.objects.filter(studentships__sponsor=sponsor)
        return SponsorDetailSerializer(students,many=True).data


class StudentSerializer(serializers.ModelSerializer):
    sponsored_money = serializers.SerializerMethodField()

    # studentships = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = StudentModel
        fields = (
            'id',
            'first_name',
            'last_name',
            'father_name',
            'student_number',
            'university',
            'student_type',
            'contract',
            'sponsored_money',
        )

    def get_sponsored_money(self, model):
        total_money = model.studentships.aggregate(money=Coalesce(Sum('money'), 0))['money']
        return total_money
    #
    # def to_representation(self, instance):
    #     student = instance['pk']
    #     data = instance.filter(sponsorships__student__id=student)
    #     return data


# class StudentDetailView(serializers.ModelSerializer):
#     class Meta:
#         model = StudentModel
#         fields = (
#             'id',
#             'first_name',
#             'last_name',
#             'father_name',
#             'student_number',
#             'university',
#             'student_type',
#             'contract',
#             'sponsored_money',
#
#         )
#         def get_date(data):
#
class StudentDetailSerializer(serializers.ModelSerializer):
    sponsorships = SponsorSerializer(many=True)
    sponsors = serializers.SerializerMethodField()

    class Meta:
        model = StudentModel
        fields = (
            'id',
            'sponsors'
            'first_name',
            'last_name',
            'father_name',
            'student_number',
            'university',
            'student_type',
            'contract',
            'sponsored_money',
        )

    def get_sponsors(self, student):
        sponsors = SponsorModel.objects.filter(sponsorships__student=student)
        return StudentDetailSerializer(sponsors, many=True).data


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = ('id', 'name')


class SponsorshipSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer(read_only=True)
    sponsor_id = serializers.IntegerField(write_only=True)
    student = StudentSerializer(read_only=True)
    student_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = SponsorshipModel
        fields = (
            'id',
            'sponsor',
            'sponsor_id',
            'student',
            'student_id',
            'money'
        )

    def create(self, validate_date):
        sponsor = get_object_or_404(SponsorModel, id=validate_date.get('sponsor_id'))
        sponsored_money = sponsor.sponsorships.aggregate(money=Coalesce(Sum('money'), 0))['money']
        student = get_object_or_404(StudentModel, id=validate_date.get('student_id'))
        student_money = student.studentships.aggregate(money=Coalesce(Sum('money'), 0))['money']
        if sponsor.enter_money - sponsored_money >= validate_date['money']:
            if student.contract - student_money >= validate_date['money']:
                instance = SponsorshipModel.objects.create(**validate_date)
                return instance
            else:
                raise ValidationError("Studentni contraktidan oshib ketadi.")
        else:
            raise ValidationError("Homiyni puli yetmay qoldi.")

    def update(self, instance, validated_data):
        sponsor = get_object_or_404(SponsorModel, id=validated_data.get('student_id'))
        sponsored_money = sponsor.sponsorships.exclude(id=instance.id).aggregate(money=Coalesce(Sum('money'), 0))[
            'money']
        sponsor_left = sponsor.enter_money - sponsored_money

        student = get_object_or_404(StudentModel, id=validated_data.get("student_id"))
        student_money = student.studentships.exclude(id=instance.id).aggregate(money=Coalesce(Sum("money", 0)))["money"]

        if validated_data['money'] <= sponsor_left:
            if student_money + validated_data['money'] <= student.contract:
                instance.money = validated_data['money']
                instance.sponsor = sponsor
                instance.student = student
                instance.save()
                return instance
            else:
                raise ValidationError("Studentni contrakti tulangan.")
        else:
            raise ValidationError("xomiyni puli yetmaydi")
