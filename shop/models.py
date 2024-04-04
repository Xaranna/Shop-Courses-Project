from django.db import models
from django.utils import timezone
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class CartQuerySet(models.QuerySet):
    def total_sum(self):
        return round(sum(item.sum() for item in self), 2)

    def total_quantity(self):

        return sum(item.quantity for item in self)


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartQuerySet.as_manager()

    def __str__(self):
        return f"Cart for {self.user.username} | Course: {self.course.title}"

    def sum(self):
        return round(self.course.price * self.quantity, 2)



