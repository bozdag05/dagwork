from django.contrib import admin
from .models import ClientModel, ContractorModel, SoftSkillsModel, HardSkillsModel, SpecializationModel
# Register your models here.


# Указываем какие поля заказчика хотим отображать на дисплее
class ClientAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "number"]


# Указываем какие поля исполнителя хотим отображать на дисплее
class ContractorAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "number", "experience"]

# В оставшихся классах всего по 1 полю, поэтому там нечего отображать


class SoftSkillsAdmin(admin.ModelAdmin):
    pass


class HardSkillsAdmin(admin.ModelAdmin):
    pass


class SpecializationAdmin(admin.ModelAdmin):
    pass


admin.site.register(ClientModel, ClientAdmin)
admin.site.register(ContractorModel, ContractorAdmin)
admin.site.register(SoftSkillsModel, SoftSkillsAdmin)
admin.site.register(HardSkillsModel, HardSkillsAdmin)
admin.site.register(SpecializationModel, SpecializationAdmin)
