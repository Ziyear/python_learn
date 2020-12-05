from django.db import models


class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDeleted=False)

    # 创建 bookInfo对象 方法2
    def create(self, title, pub_date):
        b = BookInfo()
        b.btitle = title
        b.bpub_date = pub_date
        b.bread = 0
        b.bcommet = 0
        b.isDeleted = False
        return b


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'

    books1 = models.Manager()
    books2 = BookInfoManager()

    # 创建 bookInfo对象 方法1
    @classmethod
    def create(cls, title, pub_date):
        b = cls(btitle=title, bpub_date=pub_date)
        b.bread = 0
        b.bcommet = 0
        b.isDeleted = False
        return b


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDeleted = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
