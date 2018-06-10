from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    numDocumento = models.CharField(max_length = 30, null = True, blank = True)
    area = models.CharField(max_length = 50,null = True, blank=True)
    perfil = models.IntegerField(default = 0)

    def __str___(self):
        return "perfil: %s"%(self.perfil)


    class Admin:
        pass
