from django.contrib import admin
from .models import ClientModel, ContractorModel, SoftSkillsModel, HardSkillsModel, SpecializationModel
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    pass


class ContractorAdmin(admin.ModelAdmin):
    pass


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
