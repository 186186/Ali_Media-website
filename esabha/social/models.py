from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator,RegexValidator


# Create your models here.

# create profile data
class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18,validators=[MinValueValidator(18),MaxValueValidator(100)])
    email = models.EmailField(null=True , blank=True)
    address = models.TextField()
    status = models.CharField(max_length=20, default="single", choices=(("single" , "single") ,("married","married"),("widow","widow")))
    gender = models.CharField(max_length=20, default="female", choices=(("male" , "male") ,("female","female")))
    phone_no = models.CharField(validators=[RegexValidator("0?[5-9]{1}\9{9}$")] , max_length=15,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    pic = models.ImageField(upload_to="image\\", null=True, blank= True)

    def __str__(self):
        return self.name
# create post data
class MyPost(models.Model):
    pic = models.ImageField(upload_to="image\\", null=True , blank=True)
    subjecct = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date=models.DateTimeField(auto_now_add=True)
    uploaded_by=models.ForeignKey(to=MyProfile, on_delete=CASCADE,null=True , blank=True)
    def __str__(self):
       return self.subjecct

#create PostComment data
class PostComment(models.Model):
    Post=models.ForeignKey(to=MyPost, on_delete=CASCADE)
    msg = models.TextField()
    commented_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now=True)
    flag = models.CharField(max_length=20, null=True, blank=True, choices=(("racist", "racist"), ("abbusing", "abbusing")))
    def __str__(self):
        return self.msg


# create Post Link data
class Postlike(models.Model):
    Post=models.ForeignKey(to=MyPost, on_delete=CASCADE)
    liked_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.liked_by


# create Follow user data
class FollowUser(models.Model):
    profile = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="profile")
    followed_by=models.ForeignKey(to=MyProfile,on_delete=CASCADE, related_name="followed_by")

    def __str__(self):
        return "%s is followed by %s" % (self.profile, self.followed_by)


# def __str__(self):
#     return self.followed_by