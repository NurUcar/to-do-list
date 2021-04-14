from django.db import models
from django.contrib.auth.models import User


class toDoLists(models.Model):
    user = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE)
    list_name = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.list_name


class toDoListItem(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
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

    class Meta:
        ordering = ('-created_at', '-dead_line', 'item_name', 'status')

    def __str__(self):
        return self.item_name
