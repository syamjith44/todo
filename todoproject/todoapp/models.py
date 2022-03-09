from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.title

