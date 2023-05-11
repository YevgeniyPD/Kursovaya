from django.db import models

class Baza(models.Model):
        name = models.CharField('Имя', max_length=22)
        lastname = models.CharField('Фамилия',max_length=22)
        surname = models.CharField('Отчество',max_length=22)
        citizenship = models.CharField('Гражданство',max_length=222)
        pob = models.CharField('Место рождения',max_length=32)
        dob = models.DateField('Дата рождения')
        vidDocument = models.CharField('Документ',max_length=222)
        seria = models.IntegerField('Серия')
        nomer = models.IntegerField('Номер')
        organ = models.CharField('Орган',max_length=32)
        snils = models.IntegerField('Снилс')
        phone = models.IntegerField('Номер')
        email = models.EmailField('Емайл',max_length=32)
        sogl = models.BooleanField(' - Я отношусь к льготной категории в соотвествии с пунктом 1 статьи 333.35 НК RФ')
        sogl1 = models.BooleanField(' - Даю согласие на представление персональных данных третьим лицам с целью отображения в выписке')
        req = models.CharField('Услуга',max_length=222)
        vidobject = models.CharField('Вид обьекта',max_length=222)
        adres = models.CharField('Адрес',max_length=52)
        cad_nomer = models.CharField('Кадастровый номер',max_length=24)
        documents = models.ImageField('Документы')
        prim = models.CharField('Примечание',max_length=220)
        status = models.CharField('Статус',max_length=22, default='В ожидании')
        time_create = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.cad_nomer

        class Meta:
                verbose_name = 'Запрос'
                verbose_name_plural = 'Запросы'