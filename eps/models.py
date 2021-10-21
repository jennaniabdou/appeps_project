from django.db import models




class Type(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=200, unique=True)
    activity = models.CharField(max_length=200)
    level1 = models.CharField(max_length=200)
    level2 = models.CharField(max_length=200)
    image = models.URLField()

    def __str__(self):
        return self.name



class ModuleType(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="type")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="module")

    def __str__(self):
        return self.name


