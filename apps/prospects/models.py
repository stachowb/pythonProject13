from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=128)
    eval = models.IntegerField(default=0)


class Attributes(models.Model):
    experience = models.ForeignKey(Skills, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills, through='AttributesSkills')
    user = models.ForeignKey()


class AttributesSkills(models.Model):
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    attributes = models.ForeignKey(Attributes, on_delete=models.CASCADE)
