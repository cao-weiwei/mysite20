from django.db import models

# Create your models here.
# useful packages
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Topic(models.Model):
    """ model for Topic """
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='')

    def __str__(self):
        """ overload str function """
        return "Name: {}, Category: {}".format(self.name, self.category)


class Course(models.Model):
    """ model for Course """
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    # new fields in Lab7
    interested = models.PositiveIntegerField(default=0)
    stages = models.PositiveIntegerField(default=3)

    def __str__(self):
        return "Topic: {}, Name: {}, Price: {}, For_everyone: {}, Description: {}".format(
            self.topic, self.name, self.price, self.for_everyone, self.description
        )

    def discount(self):
        """ return the discount amount of the price"""
        return self.price * 0.1


class Student(User):
    """ model for Student """
    CITY_CHOICES = [
        ('WS', 'Windsor'),
        ('CG', 'Calgery'),
        ('MR', 'Montreal'),
        ('VC', 'Vancouver')
    ]
    school = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='Windsor')
    interested_in = models.ManyToManyField(Topic)
    address = models.CharField(max_length=128, default='')

    def __str__(self):
        return "Username: {}, City:{}, Address: {}".format(self.username, self.city, self.address)


class Order(models.Model):
    ORDER_STATUS = [
        (0, 'Cancelled'),
        (1, 'Order Confirmed'),
    ]
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='students', on_delete=models.CASCADE)
    levels = models.PositiveIntegerField()
    order_status = models.IntegerField(choices=ORDER_STATUS)
    order_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Course: {}, Student: {}, Levels: {}, Order_status: {}, Order_date: {}".format(
            self.course, self.student, self.levels, self.order_status, self.order_date
        )
