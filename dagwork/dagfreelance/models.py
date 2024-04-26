from django.db import models
from django.conf import settings


# 1.Модель заказчика
# 3.Поле user со взаимосвязью один-к-одному будет использоваться для
# ассоциирования профилей с пользователями
class ClientModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Заказчик')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Заказчик')
    photo = models.ImageField(upload_to='image/users/%Y/%m/%d', blank=True, null=True, verbose_name='Фото')
    number = models.CharField(max_length=12, verbose_name='Номер')
    messages = models.TextField(blank=True, verbose_name='Соц.сети')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.user.username


# 1.Модель исполнителя
# 2.Есть связ многие-к-мнгоим с моделями SoftSkillsModel, HardSkillsModel, SpecializationModel
# 3.Поле user со взаимосвязью один-к-одному будет использоваться для
# ассоциирования профилей с пользователями
class ContractorModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Исполнитель')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='День рождение')
    photo = models.ImageField(upload_to='image/users/%Y/%m/%d', blank=True, verbose_name='Фото')
    number = models.CharField(max_length=12, verbose_name='Номер')
    messages = models.TextField(verbose_name='Соц.сети', blank=True)
    description = models.TextField(verbose_name='О себе', blank=True)
    experience = models.DateField(verbose_name='Опыт работы', blank=True, null=True)
    link_resume = models.TextField(verbose_name='Ссылки на резюме/ГИТ/ и т.д.', blank=True)
    softskills = models.ManyToManyField('SoftSkillsModel', verbose_name='гибкие навыки', blank=True,
                                        related_name='soft')
    hardskills = models.ManyToManyField('HardSkillsModel', verbose_name='профессиональные навыки', blank=True,
                                        related_name='hard')
    specialization = models.ManyToManyField('SpecializationModel', verbose_name='Специализация', blank=True,
                                            related_name='specialization')

    def __str__(self):
        return self.user.username


# Модель Софт скилы
class SoftSkillsModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='softskills')

    def __str__(self):
        return self.title


# 1.Модель Хард скилы
class HardSkillsModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='hardskills')

    def __str__(self):
        return self.title


# 1.Модель Специализации
class SpecializationModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='Специальность')

    def __str__(self):
        return self.title

