from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(unique=True,max_length=20, db_column='name')
    upwd = models.CharField(max_length=64, db_column='pwd')

    def getname(self):
        return self.uname
    

    def showme(self, name):
        return self.uname + name