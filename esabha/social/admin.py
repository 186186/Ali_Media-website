from django.contrib import admin
from .models import FollowUser,MyPost,MyProfile,PostComment,Postlike
from django.contrib.admin.options import ModelAdmin

class FollowUserAdmin(ModelAdmin):
    list_display = ["profile", "followed_by" ]
    list_filter = [ "profile", "followed_by" ]
    search_fields = ["followed_by"]

admin.site.register(FollowUser,FollowUserAdmin)

class MypostAdmin(ModelAdmin):
    list_display = ["subjecct" , "cr_date","uploaded_by"]
    search_fields =  ["uploaded_by" , "msg"]
    list_filter =  ["cr_date"]

admin.site.register(MyPost,MypostAdmin)

class MyprofileAdmin(ModelAdmin):
    list_display = ["name", "user", "email"]
    search_fields = ["name"]
    list_filter = ["user"]


admin.site.register(MyProfile, MyprofileAdmin)


admin.site.register(PostComment)

class postLikeAdmin(ModelAdmin):
    list_display = ["Post", "liked_by"]
    list_filter = ["cr_date"]

admin.site.register(Postlike, postLikeAdmin)



