from django.contrib import admin

# Register your models here.
from .models import Grades,Students
#注册
class StudentsInfo(admin.TabularInline): #StackedInline 和 TabularInline 排列方式不同
    model = Students
    extra = 0

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo] #引入 关联字段 ，创建新数据时，同时创建关联对象的数据信息
    #列表页属性
    list_display = ['gname','pk','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    #list_per_page = []
    #添加、修改页属性
    #fields = ['gdate','gname','ggirlnum','gboynum','isDelete']
    fieldsets = [
        ('base',{'fields':['gname','gdate','isDelete']}),
        ('num', {'fields': ['ggirlnum', 'gboynum']}),
     ]
admin.site.register(Grades,GradesAdmin)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    #设置页面列名
    gender.short_description = '性别'

    def name(self):
        return self.sname
    name.short_description = '姓名'

    def isd(self):
        if self.isDelete:
            return '不在职'
        else:
            return '在职'
    isd.short_description = '是否在职'

    list_display = ['id',name,gender,'sage','scontend',isd,'sgrade','lastTime','createTime']
    #fields = ['sname','sgender','sage','scontend','isDelete','sgrade']
    list_per_page = 10

    #执行动作 的位置
    actions_on_top = False
    actions_on_bottom = True
#admin.site.register(Students,StudentsAdmin)