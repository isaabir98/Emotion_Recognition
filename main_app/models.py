from django.db import models

class empInsert(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table:"user"


class user_records(models.Model):
    first_name =models.CharField(max_length=250)
    last_name =models.CharField(max_length=250)
    email =models.CharField(max_length=250)
    uname =models.CharField(max_length=250)
    pword =models.CharField(max_length=250)
    gender =models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    class Meta:
       db_table:"user"