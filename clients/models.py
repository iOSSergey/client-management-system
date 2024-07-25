from django.db import models
from datetime import date


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    mailing_name = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    address = models.TextField()
    work_phone = models.CharField(max_length=20, null=True, blank=True)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    mobile_phone = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    passport_number = models.CharField(max_length=50, null=True, blank=True)
    salutation = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    send_email = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    def age(self):
        if self.birth_date is None:
            return "??"
        today = date.today()
        age = today.year - self.birth_date.year - \
            ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def age_with_suffix(self):
        age = self.age()
        if age == "??":
            return age
        elif age == 1:
            return f"{age} year"
        else:
            return f"{age} years"

    def trip_count(self):
        return self.trips.count()

    # class Meta:
    #     db_table = 'ClientBase'


# class Country(models.Model):
#     n = models.AutoField(db_column='N', primary_key=True)
#     value = models.CharField(db_column='Value', unique=True, max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'Country'


# class Type(models.Model):
#     n = models.SmallAutoField(db_column='N', primary_key=True)
#     value = models.CharField(db_column='Value', max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'Type'
