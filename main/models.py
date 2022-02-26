from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class SponsorModel(models.Model):
    STATUS = (
        ('new', 'new'),
        ('approved', 'approved'),
        ('moderation', 'moderation'),
        ('canceled', 'canceled'),
    )
    Choice_Money = (
        ('1_000_000', '1_000_000'),
        ('5_000_000', '5_000_000'),
        ('7_000_000', '7_000_000'),
        ('10_000_000', '10_000_000'),
        ('30_000_000', '30_000_000'),
    )
    Person_Type = (
        ('legal', 'legal'),
        ('physical', 'physical'),
    )
    Pay_Type = (
        ('cash', 'cash'),
        ('card', 'card'),
        ('salary', 'salary'),
    )
    person_type = models.CharField(max_length=100, choices=Person_Type, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    sponsor_number = models.CharField(max_length=13, null=True)
    choice_money = models.CharField(max_length=100, choices=Choice_Money, null=True)
    enter_money = models.PositiveIntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, null=True)
    pay_type = models.CharField(max_length=100, choices=Pay_Type, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"
        ordering = ['-created_date']


class UniversityModel(models.Model):
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "University"
        verbose_name_plural = "Universities"


class StudentModel(models.Model):
    Student_Type = (
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('Phd', 'Phd'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=200, null=True, blank=True)
    student_type = models.CharField(max_length=100, choices=Student_Type, null=False)
    university = models.ForeignKey(UniversityModel, on_delete=models.PROTECT)
    contract = models.PositiveIntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Student"
        verbose_name_plural = "Students"


class SponsorshipModel(models.Model):
    sponsor = models.ForeignKey(SponsorModel, on_delete=models.CASCADE, related_name='sponsorships')
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name='studentships')
    money = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sponsor: {self.sponsor} ->to  Student: {self.student}"

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Sponsorship"
        verbose_name_plural = "Sponsorships"


