from django.db import models
from django.contrib.auth.models import User


class toDoLists(models.Model):
    user = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE)
    list_name = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class toDoListItem(models.Model):
    STATUS = (
        ('Complete', 'Complete'),
        ('On Progress', 'On Progress'),
        ('Expired', 'Expired'),
    )
    toDoList = models.ForeignKey(
        toDoLists, related_name="toDoList", on_delete=models.CASCADE)
    item_name = models.TextField(null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15, choices=STATUS, default='On Progress')
    dead_line = models.DateTimeField()
