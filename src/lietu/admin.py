from django.contrib import admin
from .models import DogInfo, DogGroup, Mountain


class DogInfoAdmin(admin.ModelAdmin):
    list_display = ('dog_name', 'dog_group', 'dog_trainer', 'use_times', 'work_zan', 'create_time')
    exclude = ('work_zan', 'create_time', 'modified_time', 'use_times', 'condition', 'dog_trainer')
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.dog_trainer = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(DogInfoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(dog_trainer=request.user.id)


admin.site.register(DogInfo, DogInfoAdmin)
admin.site.register(DogGroup)
admin.site.register(Mountain)
admin.site.site_header = '猎兔运维辅助平台'
admin.site.site_title = '猎兔运维辅助平台'
