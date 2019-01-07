from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return "%s-%d-%d"%(self.gname,self.ggirlnum,self.gboynum)

#自定义 管理器类
class StudentsManger(models.Manager):
    def get_queryset(self):
        return super(StudentsManger,self).get_queryset().filter(isDelete=False)
    def createStudent(self,name,age,gender,contend,grade):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        return stu

class Students(models.Model):
    #自定义 管理器 属性
    stuObj = models.Manager()
    stuObj1 = StudentsManger()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False,db_column='isdelete')
    lastTime = models.DateTimeField(auto_now=True,db_column='lasttime')
    createTime = models.DateTimeField(auto_now_add=True,db_column='createtime')
    # 关联外键
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)
    def __str__(self):
        return self.sname
    def getname(self):
        return self.sname
    class Meta:
        ordering = ['-id']

    #定义一个类方法 创建对象
    @classmethod
    def createStudent(cls,name,age,gender,contend,grade,isD=False):
        stu = cls(sname=name,sage=age,sgender=gender,scontend=contend,sgrade=grade,isDelete=isD)
        return stu