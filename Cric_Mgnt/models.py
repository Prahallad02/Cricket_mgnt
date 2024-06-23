from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Common(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

Coach_Choices = (
    ("Batting","Batting"),
    ("Bowling" , "Bowling"),
    ("FieldCoach","FiledCoach"),
    ("Psyhsio","Psyhsio")
)

Players_Choice = (
    ("Batting","Batting"),
    ("Bowling" , "Bowling"),
    ("AllRounder" , "AllRounder")

)

class CoachModel(Common):
    specialty = models.CharField( max_length=20, default=None , choices=Coach_Choices)
    profile_pic = models.ImageField(upload_to='Coach',blank = True , null=True , default='demo.jpg')
    experience = models.CharField(max_length=15)

    class Meta:
        db_table ='cric_mgnt_coachmodel'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class PlayersModel(Common):
    matches_played = models.IntegerField(default=0)
    coached_by = models.ForeignKey(CoachModel, on_delete=models.CASCADE, default=None)
    high_score = models.BigIntegerField(default=0)
    high_wic = models.IntegerField(default=0)
    specialty = models.CharField( max_length=20 ,  default=None , choices=Players_Choice)
    profile_pic = models.ImageField(upload_to='Players',blank = True , null=True , default='demo.jpg')
    
    class Meta:
        db_table ='cric_mgnt_playersmodel'

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
class RegisterModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def set_password(self,raw_password):
        self.password = make_password(raw_password)

    def check_password(self,raw_password):
        return check_password(raw_password,self.password)


    class Meta:
        db_table ='register'
 
    def __str__(self):
        return {self.name}
    
    
class LoginModel(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    class Meta:
        db_table ='login'
 
    def __str__(self):
        return {self.email}

