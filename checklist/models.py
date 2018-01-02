from django.db import models


class ListTemplate(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ListItemTemplate(models.Model):
    name = models.CharField(max_length=250)
    itemIsChecked = models.BooleanField(default=False)
    list = models.ForeignKey('ListTemplate', on_delete=models.CASCADE)


class List(models.Model):
    name = models.CharField(max_length=250)


class Item(models.Model):
    name = models.CharField(max_length=250)
    itemIsChecked = models.BooleanField(default=False)
    list = models.ForeignKey('List', on_delete=models.CASCADE)
