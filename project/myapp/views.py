from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Students

# Create your views here.
from django.http import HttpResponse
def index(request):
    #return HttpResponse("hello world")
    student = Students.stuObj1.get(pk = 1)
    return render(request,'myapp/index.html',{'stu':student,'num':10,'str':'strs','list':['good','nice','handsome'],'test':10})
def detail(request,num):
    return HttpResponse("detail - %s"%num)

from .models import Grades,Students
def grades(request):
    #去模型里取数据
    gradeList = Grades.objects.all()
    #将数据传递给模板，渲染成页面,返回给用户
    return render(request,'myapp/grades.html',{'grades':gradeList})

def students(request):
    #去模型里取数据
    studentsList = Students.stuObj1.all()
    #将数据传递给模板，渲染成页面,返回给用户
    return render(request,'myapp/students.html',{'students':studentsList})

#显示前5条学生
def students3(request):
    studentsList = Students.stuObj1.all()[0:5]
    return render(request, 'myapp/students.html', {'students': studentsList})

#分页显示学生
def stupage(request,page):
    #0-5 5-10 10-15
    # 1   2     3
    page = int(page)
    studentsList = Students.stuObj1.all()[(page-1)*5:page*5]
    return render(request, 'myapp/students.html', {'students': studentsList})

from django.db.models import Max,Q
def studentssearch(request):
    #studentsList = Students.stuObj1.all().filter(sname__contains="张")
    #studentsList = Students.stuObj1.all().filter(sname__startswith="张")
    #studentsList = Students.stuObj1.all().filter(sname__endswith="1")
    #studentsList = Students.stuObj1.all().filter(id__in=[1,2,4,5,10])
    #studentsList = Students.stuObj1.all().filter(sage__gt=30)
    #studentsList = Students.stuObj1.all().filter(lastTime__year=2017)
    #studentsList = Students.stuObj1.all().filter(sname__contains="%")
    #描述中带有"薛艳梅"这三个字的数据属于哪一个班级的
    grade = Grades.objects.all().filter(students__scontend__contains="薛艳梅")
    print(grade)
    #maxAge = Students.stuObj1.aggregate(Max("sage"))
    #studentsList = Students.stuObj1.all().filter(sage=maxAge.get('sage__max'))

    studentsList =Students.stuObj1.filter(Q(pk__lt=5) | Q(sage__gt=50))

    return render(request,'myapp/students.html',{'students':studentsList})


def gradesstudents(request,num):
    #获得对应的班级对象
    grade = Grades.objects.get(pk=num)
    #获得班级下的所有学生信息列表
    studentsList = grade.students_set.all()
    return render(request, 'myapp/students.html', {'students': studentsList})

def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("刘德华",34,True,"我叫刘德华",grade,)
    stu.save()
    return HttpResponse("保存")

def addstudent1(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj1.createStudent("张学友1",22,True,"我就张学友",grade)
    stu.save()
    return HttpResponse("保存")


from django.db.models import F
def grades1(request):
    g = Grades.objects.filter(ggirlnum__gt=F("gboynum"))
    print(g)
    return HttpResponse(g)

def attriblues(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)

    return HttpResponse("attriblues")

#获取get传递的数据
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + ' ' + b + ' ' + c)

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + ' ' + a2 + ' ' + c)

#POST
def showregist(request):
    return render(request,'myapp/regist.html')
def regist(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse(str(name))

#Responese
def showresponse(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    return res


#cookie
def cookietest(request):
    res = HttpResponse()
    cookie = res.set_cookie('sunck','good')
    return res
def showcookie(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write('<h1>'+cookie['sunck']+'</h1>')
    return res

#重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirect1(request):
    return redirect('/redirect2')
    #return HttpResponseRedirect('/redirect2')
def redirect2(request):
    return HttpResponse('我是重定向后的视图')

#用户登录session
def main(request):
    #取session
    username = request.session.get('name','游客')
    print(username)
    return render(request,'myapp/main.html',{'username':username})
def login(request):
    return render(request,'myapp/login.html')
def showmain(request):
    print('******')
    username = request.POST.get('username')
    #存储session
    request.session['name']=username
    request.session.set_expiry(10)#10秒后过期
    return redirect('/main')
from django.contrib.auth import logout
def quit(request):
    #清除session
    logout(request)
    #request.session.clear()
    #request.session.flush()
    return redirect('/main')



def get_classes(request):
    cls_list = Grades.objects.all()
    return render(request, 'myapp/get_classes.html', {'cls_list': cls_list})
def add_classes(request):
    if request.method == "GET":
        return render(request, 'myapp/add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('titile')
        Grades.objects.create(gname=title)
        return redirect('myapp/get_classes.html')
def del_classes(request):
    nid = request.GET.get('nid')
    Grades.objects.filter(id=nid).delete()
    return redirect('myapp/get_classes.html')
def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = Grades.objects.filter(id=nid).first()
        return render(request, 'myapp/edit_classes.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        Grades.objects.filter(id=nid).update(gname=title)
        return redirect('myapp/get_classes.html')


def good(request,num):
    return render(request,'myapp/good.html',{'num':num})

def mainbase(request):
    return render(request,'myapp/mainbase.html')