from django.contrib import admin
from .models import Plans,current_plan
# Register your models here.
class plans(admin.ModelAdmin):
    list_display=('Plan_Name','Mobile','Basic','Standard','Premium')
admin.site.register(Plans,plans)

class cp(admin.ModelAdmin):
    list_display=('Plan_Name','price','subscription')
admin.site.register(current_plan,cp)