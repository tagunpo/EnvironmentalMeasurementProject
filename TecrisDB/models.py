from django.db import models

# Create your models here.

#テクリス関連
class TECRIS_CLASS_CODE(models.Model):
    """テクリス区分コード"""
    tecris_class_code = models.CharField(primary_key=True,verbose_name='テクリス区分コード',max_length=1,null=False,blank=False)
    tecris_class_name= models.CharField(verbose_name='区分',max_length=8,null=False,blank=False)
    def __str__(self):
        return f'{self.tecris_class_code}:{self.tecris_class_name}'

    class Meta:
        verbose_name = 'テクリス区分コード'
        verbose_name_plural = 'テクリス区分コード'

class TECRIS_RIVER_TYPE_CODE(models.Model):
    """テクリス河川種類コード"""
    tecris_river_type_code = models.CharField(primary_key=True,verbose_name='テクリス河川種類コード',max_length=1,null=False,blank=False)
    tecris_water_system_class= models.CharField(verbose_name='水系区分',max_length=16,null=False,blank=False)
    tecris_river_type = models.CharField(verbose_name='河川種類',max_length=16,null=False,blank=False)
    def __str__(self):
        return f'{self.tecris_river_type_code}:{self.tecris_river_type}'



    class Meta:
        verbose_name = 'テクリス河川種類コード'
        verbose_name_plural = 'テクリス河川種類コード'

class TECRIS_WATER_SYSTEM_CODE(models.Model):

    tecris_water_system_code = models.CharField(primary_key=True,verbose_name='テクリス一級水系番号',max_length=3,null=False,blank=False)
    tecris_water_system = models.CharField(verbose_name='水系名', max_length=16, null=False, blank=False)
    tecris_class_code = models.ForeignKey(TECRIS_CLASS_CODE,verbose_name='テクリス区分コード', on_delete=models.SET_NULL, null=True,
                                         blank=True)
    tecris_river_type_code = models.ForeignKey(TECRIS_RIVER_TYPE_CODE, verbose_name='テクリス河川種類コード', on_delete=models.SET_NULL, null=True,
                                              blank=True)
    def __str__(self):
        return f'{self.tecris_water_system_code}:{self.tecris_water_system}'

    class Meta:
        verbose_name = 'テクリス水系コード'
        verbose_name_plural = 'テクリス水系コード'
