from django_filters.rest_framework import FilterSet
from main.models import (
    SponsorModel,
    StudentModel,
    UniversityModel,
    SponsorshipModel,
)


class SponsorFilter(FilterSet):
    class Meta:
        model = SponsorModel
        fields = (
            'status',
            'enter_money',
            'updated_date',
        )
