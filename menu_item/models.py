from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='submenu')

    def __str__(self):
        return self.title
