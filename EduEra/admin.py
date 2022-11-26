from django.contrib import admin
# Register your models here.
from EduEra.models import studentForm, teacherForm
from .models import RoomMember


admin.site.register(RoomMember)
admin.site.register(teacherForm)
admin.site.register(studentForm)
