from django.shortcuts import render,redirect
from .forms import UserForm,UPForm,AdUserForm,AdupForm,BookingForm,UpbookForm,ChangePassForm,FBForm,PayForm,StsalForm,FeeForm
from .models import User,Booking,Feedback,Payment,Staff,RoomFee
from django.contrib import messages
from django.core.mail import send_mail
from hms import settings
from datetime import datetime,date
#import datetime

# Create your views here.
def home(request):
    return render(request,'html/home.html')

def about(request):
    return render(request,'html/about.html')

def contact(request):
    return render(request,'html/contact.html')

def register(request):
    if request.method=="POST":
        f=UserForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/')
    else:
        f=UserForm()
    return render(request,'html/register.html',{'g':f})

def mailsend(request):
    if request.method=="POST":
        sender=request.POST['sn']
        subject=request.POST['sb']
        desc=request.POST['msg']
        t=settings.EMAIL_HOST_USER
        b=send_mail(subject,desc,t,[sender])
        if b==1:
            messages.success(request,"Mail sent successfully!!")
            return redirect('/mail')
        else:
            messages.warning(request,"Mail not sent!!")
            return redirect('/mail')
    return render(request,'html/mail.html')

def userlist(request):
    c=User.objects.all()
    n,m={},{}
    txt=""
    if request.method=="POST":
        s=AdUserForm(request.POST)
        if s.is_valid():
            r1=s.cleaned_data['role1']
            r2=s.cleaned_data['role2']
            if r1=='Guest' or r1=='User':
                if r2=='0':
                    s.save()
                    messages.success(request,'User Created successfully!!')
                else:
                    txt="Invalid Role Types"
            elif r1=='Staff':
                if r2!='0':
                    s.save()
                    messages.success(request,'User Created successfully!!')
                else:
                    txt="Invalid Role Types"
            else:
                txt="Invalid Role Types"
            if txt=="Invalid Role Types":
                return render(request,'html/userlist.html',{'w':s,'k':c,'ab':txt})
            else:
                return redirect('/userlist')
        else:
            n[s]=s.errors
    for j in n.values():
        for v in j.items():
            m[v[0]]=v[1]
    s=AdUserForm()
    print(txt)
    return render(request,'html/userlist.html',{'w':s,'p':m.items(),'k':c})

def delete(request,t):
    y=User.objects.get(id=t)
    if request.method=='POST':
        y.delete()
        return redirect('/userlist')
    return render(request,'html/delete.html',{'p':y})

def update(request,d):
    k=User.objects.get(id=d)
    if request.method == "POST":
        y=AdupForm(request.POST,instance=k)
        if y.is_valid():
            y.save()
        return redirect('/userlist/')
    y=AdupForm(instance=k)
    return render(request,'html/update.html',{'x':y})

def profile(request):
    return render(request,'html/profile.html')

def updprofile(request):
    k=User.objects.get(id=request.user.id)
    if request.method=="POST":
        h=UPForm(request.POST,request.FILES,instance=k)
        if h.is_valid():
            b=h.save(commit=False)
            b.pfupd=1
            b.save()
            return redirect('/profile')
    h=UPForm(instance=k)
    return render(request,'html/updprofile.html',{'e':h})

def dashboard(request):
    return render(request,'html/dashboard.html')

def booking(request,b):
    if request.method == "POST":
        x=BookingForm(request.POST,request.FILES)
        if x.is_valid():
            sd0=x.cleaned_data['startdate']
            ed0=x.cleaned_data['enddate']
            sd=datetime.strptime(str(sd0),"%Y-%m-%d")
            ed=datetime.strptime(str(ed0),"%Y-%m-%d")
            print(ed,sd,ed>sd)
            if ed>sd:
                b=x.save(commit=False)
                b.guest_id=request.user.id
                b.save()
                return redirect('/pay')
            else:
                te="Invalid start date and end date"
                return render(request,'html/booking.html',{'b':x,'t':te})
    x=BookingForm()
    return render(request,'html/booking.html',{'b':x})

def prices(request):
    r=RoomFee.objects.all()

    return render(request,'html/prices.html',{'x':r})


def rblist(request):
    b=Booking.objects.all()
    p=Payment.objects.all()
    return render(request,'html/rblist.html',{'r':b,'s':p})

def rbupdate(request,u):
    b=Booking.objects.get(id=u)
    if request.method=="POST":
        c=UpbookForm(request.POST,instance=b)
        if c.is_valid():
            c.save()
            return redirect('/rblist')
    c=UpbookForm()
    return render(request,'html/rbupdate.html',{'r':c})

def rbdelete(request,d):
    p=Booking.objects.get(id=d)
    q=Payment.objects.get(id=d)
    if request.method == "POST":
        p.delete()
        q.delete()
        return redirect('/rblist')
        #return render(request,'html/prevbookings.html',{'k':p})
    return render(request,'html/rbdelete.html',{'k':p})

def prevbookings(request):
    s=Booking.objects.filter(guest_id=request.user.id)
    p=Payment.objects.filter(pay_id=request.user.id)
    return render(request,'html/prevbookings.html',{'k':s,'t':p})

def grupdate(request,g):
    e=Booking.objects.get(id=g)
    if request.method=="POST":
        f=BookingForm(request.POST,request.FILES,instance=e)
        if f.is_valid():
            f.save()
            return redirect('/prevbookings')
    f=BookingForm(instance=e)
    return render(request,'html/grupdate.html',{'h':f})

def changepass(request):
    c=User.objects.get(id=request.user.id)
    n,m={},{}
    if request.method=="POST":
        f=ChangePassForm(request.POST,instance=c)
        if f.is_valid():
            f.save()
            return redirect('/login')
        else:
            n[f]=f.errors
    for j in n.values():
        for v in j.items():
            m[v[0]]=v[1]
    f=ChangePassForm()
    print(m.values())
    return render(request,'html/changepass.html',{'n':f,'p':m.values()})

def duty(request):
    return render(request,'html/duty.html')


def feedback(request):
    return render(request,'html/feedback.html')

def prevfb(request):
    k=Feedback.objects.filter(feed_id=request.user.id)
    return render(request,'html/prevfeedback.html',{'m':k})

def givefb(request):
    if request.method=="POST":
        x=FBForm(request.POST)
        if x.is_valid():
            p=x.save(commit=False)
            p.feed_id=request.user.id
            p.save()
            return redirect('/feedback')
    x=FBForm()
    return render(request,'html/review.html',{'y':x})

def stafffb(request):
    p=Feedback.objects.all()
    l1=[]
    l2=[]
    n=[]
    l3=[]
    y=[]
    for i in p:
        if(i.fdtp==request.user.role2):
            r=i
            k=User.objects.filter(id=r.feed_id)
            l1.append(k)
            l2.append(i)
    for i in l1:
        n.append(i[0])
    for i in p:
        x=User.objects.filter(id=i.feed_id)
        l3.append(x)
    
    for i in l3:
        y.append(i[0])
    return render(request,'html/stafffb.html',{'v':l2,'s':n,'t':p,'u':y})

# def updfb(request,z):
#     b=Feedback.objects.filter(feed_id=request.user.id)
#     if request.method == "POST":
#         a=FBForm(request.POST,instance=b)
#         if a.is_valid():
#             a.save()
#             return redirect('/prevfb')
#     a=FBForm(instance=b)
#     return render(request,'html/updfb.html',{'c':a})

def delfb(request,z):
    b=Feedback.objects.get(id=z)
    if request.method=="POST":
        b.delete()
        return redirect('/prevfb')
    #print(b.fdtp)
    return render(request,'html/delfb.html',{'d':b})

def salary(request):
    x=Staff.objects.all()
    return render(request,'html/salary.html',{'y':x})

def roomnum(request):
    l1=[]
    l2=[]
    dic={}
    t=""
    dic1={}
    dic2={}
    dic3={}
    dic4={}
    for i in range(101,911):
        if (i-1)%100 ==0:
            for j in range(0,8):
                l1.append(i+j)
                if (i+j)%4==1:
                    t="1A"
                elif(i+j)%4==2:
                    t="1N"
                elif (i+j)%4==3:
                    t="2A"
                elif (i+j)%4==0:
                    t="2N"
                l2.append(t)
                dic[i+j]=t
    for i in dic:
        if dic[i]=="1A":
            dic1[i]="1A"
        elif dic[i]=="1N":
            dic2[i]="1N"
        elif dic[i]=="2A":
            dic3[i]="2A"
        elif dic[i]=="2N":
            dic4[i]="2N"
    b1=Booking.objects.all()
    for i in b1:
        if i.enddate<date.today():
            i.delete()
    c=0
    l=[]
    b=Booking.objects.all()
    for i in b:
        l.append(i.rbtype)
    l2=[]
    for i in b:
        l2.append(i.rnum)
    for i in l:
        for j in dic:
            J=str(j)
            if i==dic[j] and J not in l2:
                if j%100==1 and i in dic1:
                    if i==dic1[j]:
                        del dic1[j]
                elif j%100==2 and i in dic2:
                    if i==dic2[j]:
                        del dic2[j]
                elif j%100==3 and i in dic3:
                    if i==dic3[j]:
                        del dic3[j]
                elif j%100==4 and i in dic4:
                    if i==dic4[j]:
                        del dic4[j]
                if b[c].rbstatus=='a' and b[c].rnum == '':
                    b[c].rnum=j
                    b[c].save()
                elif b[c].rbstatus=='a' and b[c].rnum!="not alloted" and b[c].rnum!='':
                    b[c].rnum=b[c].rnum
                    b[c].save()
                elif b[c].rbstatus=='a' and b[c].rnum=="not alloted":
                    b[c].rnum=j
                    b[c].save()
                else:
                    b[c].rnum="not alloted"
                    b[c].save()
                c=c+1
                break
    #print(l)
    nm=[]
    for i in b:
        m=User.objects.get(id=i.guest_id)
        nm.append(m.username)
    return render(request,'html/roomnum.html',{'n':b,'q':nm})

def fee(request):
    b=Booking.objects.all()
    r=RoomFee.objects.all()
    d=[]
    di={}
    for i in r:
        di[i.rtp]=int(i.rfee)
    #print(di)
    for i in b:
        #print(i.startdate,i.enddate)
        sd=datetime.strptime(str(i.startdate),"%Y-%m-%d")
        ed=datetime.strptime(str(i.enddate),"%Y-%m-%d")
        if ed<sd:
            diff=-1
        else:
            diff=ed-sd
        # if diff==-1:
        #     print("Invalid")
        # else:
        #     print(f"{diff.days} days")
        s=i.rbtype
        # if s=="2A":
        #     f=2000
        # elif s=="2N":
        #     f=1500
        # elif s=="1A":
        #     f=3000
        # elif s=="1N":
        #     f=1800
        #print(f"{f*diff.days}")
        f=di[s]
        i.amt=f*diff.days
        i.save()
        d.append(diff.days)
    l2=[]
    for i in b:
        m=User.objects.get(id=i.guest_id)
        l2.append(m.username)
    #print(l2)
    #print(d)
    return render(request,'html/fee.html',{'a':b,'c':d,'q':l2,'f':r})

def payment(request):
    l=[]
    a=Booking.objects.all()
    for i in a:
        x=i.guest_id
        g=User.objects.get(id=x)
        l.append(g.username)
    #print(l)
    if request.method == "POST":
        q=PayForm(request.POST,request.FILES)
        if q.is_valid():
            x=q.save(commit=False)
            x.pay_id=request.user.id
            x.save()
            return redirect('/roomnum')
    q=PayForm()
    return render(request,'html/payment.html',{'p':q})

def allpayments(request):
    p=Payment.objects.all()
    if request.method=="POST":
        q=Payment.objects.filter(pay_id=request.user.id)
        q.delete()
        return redirect("/allpay")
    return render(request,'html/allpayments.html',{'a':p})

def staff(request):
    u=User.objects.all()
    s=Staff.objects.all()
    l1=[]
    l2=[]
    for i in u:
        if i.role1 == "Staff":
            l1.append(i.username)
    for i in s:
        l2.append(i.stn)
    for i in u:
        if i.username not in l2:
            if i.role1=="Staff":
                if i.role2=="Receptionist":
                    a=20000
                if i.role2=="House Keeping":
                    a=10000
                elif i.role2=="Porter":
                    a=5000
                elif i.role2=="Restaurant Staff":
                    a=15000
                b=Staff(stn=i.username,sttp=i.role2,st_id=i.id,salary=a)
                b.save()
    return render(request,'html/staff.html')

def updsalary(request,d):
    k=Staff.objects.get(id=d)
    if request.method=="POST":
        f=StsalForm(request.POST,instance=k)
        if f.is_valid():
            f.save()
            return redirect('/salary')
    f=StsalForm(instance=k)
    return render(request,'html/updsal.html',{'g':f})

def crdsalary(request,d):
    k=Staff.objects.get(id=d)
    k.crsal=k.salary+","+k.crsal
    k.status="Credited"
    k.save()
    return redirect('/salary')

def rooms(request):
    l1=[]
    l2=[]
    for i in range(101,911):
        if (i-1)%100 ==0:
            for j in range(0,8):
                l1.append(i+j)
                if (i+j)%4==1:
                    l2.append("1A")
                elif(i+j)%4==2:
                    l2.append("1N")
                elif (i+j)%4==3:
                    l2.append("2A")
                elif (i+j)%4==0:
                    l2.append("2N")
    #print(l1,l2)
    b=Booking.objects.all()
    l3=[]
    s=[]
    e=[]
    for i in b:
        l3.append(i.rnum)
        s.append(i.startdate)
        e.append(i.enddate)
    l4=[]
    print(l3)
    for i in l3:
        if i=="not alloted":
            l4.append(-1)
        elif i=='':
            l4.append(0)
        else:
            l4.append(int(i))
    print(l4)
    m=max(l4)
    ml=(m%100+1)
    stt=[]
    sd=[]
    ed=[]
    s1,e1=0,0
    td=date.today()
    print(m)
    for c in range(101,max(l4)+1):
        if(c%100<8):
            if c in l4 and e[e1]>td:
                stt.append("alloted")
                sd.append(s[s1])
                ed.append(e[e1])
                s1+=1
                e1+=1
            else:
                stt.append("not alloted")
                sd.append("")
                ed.append("")
                

            # if c not in l4:
            #     #print(c)
            #     stt.append("not alloted")
            #     sd.append("")
            #     ed.append("")
            # elif e[e1]>td:
            #     #print(c)
            #     stt.append("alloted")
            #     sd.append(s[s1])
            #     ed.append(e[e1])
            #     s1+=1
            #     e1+=1
    #print(stt[:10])
    print(sd,ed)
    return render(request,'html/rooms.html',{'x':l1,'y':l2,'z':stt,'x1':sd,'y1':ed})

def dates(request):
    d=date.today()
    dx=datetime.strptime(str(d),"%Y-%m-%d")
    b=Booking.objects.all()
    l1=[]
    l2=[]
    dic={}
    t=""
    dic1={}
    dic2={}
    dic3={}
    dic4={}
    for i in range(101,911):
        if (i-1)%100 ==0:
            for j in range(0,8):
                l1.append(i+j)
                if (i+j)%4==1:
                    t="1A"
                elif(i+j)%4==2:
                    t="1N"
                elif (i+j)%4==3:
                    t="2A"
                elif (i+j)%4==0:
                    t="2N"
                l2.append(t)
                dic[i+j]=t
    for i in dic:
        if dic[i]=="1A":
            dic1[i]="1A"
        elif dic[i]=="1N":
            dic2[i]="1N"
        elif dic[i]=="2A":
            dic3[i]="2A"
        elif dic[i]=="2N":
            dic4[i]="2N"

    l3=[]
    l=[]
    for i in b:
        l3.append(i.rnum)
        l.append(i.rbtype)
    for i in l3:
        i=int(i)
        if i%4==1:
            #print(i)
            del dic1[i]
        elif i%4==2:
            del dic2[i]
        elif i%4==3:
            del dic3[i]
        elif i%4==0:
            del dic4[i]
    for j in b:
        sd=datetime.strptime(str(j.startdate),"%Y-%m-%d")
        ed=datetime.strptime(str(j.enddate),"%Y-%m-%d")
        if(dx>ed):
            i=int(j.rnum)
            k=j.rbtype
            if i%4==1:
                i=str(i)
                dic1[i]=k
            elif i%4==2:
                i=str(i)
                dic2[i]=k
            elif i%4==3:
                i=str(i)
                dic3[i]=k
            elif i%4==0:
                i=str(i)
                dic4[i]=k
            else:
                print(0)
            j.delete()
    
    dx=str(dx)
    print(dx)
    dt=(dx[:10])
    return render(request,'html/dates.html',{'x':dt})


def roomfee(request):
    r=RoomFee.objects.all()
    l1=[]
    for i in r:
        l1.append(i.rtp)
    print(l1)
    if request.method=="POST":
        f=FeeForm(request.POST)
        if f.is_valid():
            a=f.cleaned_data['rtp']
            b=f.cleaned_data['rfee']
            count=0
            for i in b:
                if i.isdigit():
                    count=1
                    continue
                else:
                    count=0
                    break
            if count==1:
                if a in l1:
                    r1=RoomFee.objects.get(rtp=a)
                    r1.rfee=b
                    r1.save()
            
        return redirect('/prices')
    f=FeeForm()
    return render(request,'html/roomfee.html',{'x':f})