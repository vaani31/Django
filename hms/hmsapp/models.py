from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    gn=[
        ('0','---Select Gender---'),
        ('1','Female'),
        ('2','Male')
    ]
    ro1=[
        ('Guest','Guest'),
        ('User','User'),
        ('Staff','Staff'),
    ]
    ro2=[
        ('0','---Select Staff Type---'),
        ('Receptionist','Receptionist'),
        ('House Keeping','House Keeping'),
        ('Porter','Porter'),
        ('Restaurant Staff','Restaurant Staff'),
    ]
    cid=models.CharField(max_length=10,default="")
    gndr=models.CharField(choices=gn,default='0',max_length=10)
    role1=models.CharField(choices=ro1,default='Guest',max_length=10)
    role2=models.CharField(choices=ro2,default='0',max_length=20)
    mbl=models.CharField(max_length=10,default="")
    adrs=models.CharField(max_length=200,default="")
    pfimag=models.ImageField(upload_to='Profiles/',default='prof.png')
    dob=models.DateField(null=True,blank=True)
    pfupd=models.BooleanField(default=False)

class Booking(models.Model):
    s=[
        ('p',"Pending"),
        ('a','Approved'),
        ('d','Declined'),
    ]
    i=[
        ('ip','---Select Id Proof Type---'),
        ('a','Aadhar Card'),
        ('p','PAN Card'),
        ('l','Licence'),
        ('v','Voter Card'),
        ('g','Other Government Certificate'),
    ]
    t=[
        ('0','---Select Room Type---'),
        ('1A','1-Adult/Room(AC)'),
        ('2A','2-Adults/Room(AC)'),
        ('1N','1-Adult/Room(Non-AC)'),
        ('2N','2-Adults/Room(Non-AC)'),
    ]
    rbstatus=models.CharField(choices=s,default='p',max_length=10)
    rbtype=models.CharField(choices=t,default='0',max_length=10)
    startdate=models.DateField()
    enddate=models.DateField()
    apldate=models.DateField(auto_now_add=True)
    mgdesc=models.CharField(max_length=200)
    idproof=models.CharField(choices=i,default='ip',max_length=15)
    idatch=models.FileField(upload_to='Attachments/')
    rnum=models.CharField(max_length=10,default="")
    amt=models.CharField(max_length=10,default="")
    guest=models.ForeignKey(User,on_delete=models.CASCADE)


class Feedback(models.Model):
    t=[
        ('0','---Select Staff Type---'),
        ('Receptionist','Receptionist'),
        ('House Keeping','House Keeping'),
        ('Porter','Porter'),
        ('Restaurant Staff','Restaurant Staff'),
    ]
    fdtp=models.CharField(choices=t,default='0',max_length=20)
    fd=models.CharField(max_length=200)
    feed=models.ForeignKey(User,on_delete=models.CASCADE)

class Payment(models.Model):
    payatch=models.FileField(upload_to='Attachments/')
    pay=models.ForeignKey(User,on_delete=models.CASCADE)

class Staff(models.Model):
    t=[
        ('0','---Select Staff Type---'),
        ('Receptionist','Receptionist'),
        ('House Keeping','House Keeping'),
        ('Porter','Porter'),
        ('Restaurant Staff','Restaurant Staff'),
    ]
    stn=models.CharField(max_length=20)
    sttp=models.CharField(choices=t,default='0',max_length=20)
    salary=models.CharField(max_length=10)
    crsal=models.CharField(max_length=20)
    status=models.CharField(max_length=200,default="")
    st=models.ForeignKey(User,on_delete=models.CASCADE)

class RoomFee(models.Model):
    t=[
        ('0','---Select Room Type---'),
        ('1A','1-Adult/Room(AC)'),
        ('2A','2-Adults/Room(AC)'),
        ('1N','1-Adult/Room(Non-AC)'),
        ('2N','2-Adults/Room(Non-AC)'),
    ]
    rtp=models.CharField(choices=t,default='0',max_length=10)
    rfee=models.CharField(max_length=10)
