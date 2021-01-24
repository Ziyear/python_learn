from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=40)
    isDeleted = models.BooleanField()


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDeleted = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    level_id = models.IntegerField()
    parea_id = models.IntegerField()
