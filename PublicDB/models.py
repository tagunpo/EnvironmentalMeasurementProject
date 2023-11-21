from django.db import models
#
# # Create your models here.
#
class SURVEY_POSITION_CODE_PUBLIC(models.Model):
    code = models.CharField(primary_key=True,verbose_name='採取位置コード（公共用水域及び地下水の水質測定計画）',max_length=2)
    position = models.CharField(verbose_name='採取位置',max_length=16,null=False,blank=False)

    def __str__(self):
        return f'{self.code}:{self.position}'

    class Meta:
        verbose_name = '採取位置コード（公共用水域及び地下水の水質測定計画）'
        verbose_name_plural = '採取位置コード（公共用水域及び地下水の水質測定計画）'

class WEATHER_CODE_PUBLIC(models.Model):
    code = models.CharField(primary_key=True,verbose_name='天候コード（公共用水域及び地下水の水質測定計画）',max_length=2)
    weather = models.CharField(verbose_name='天候', max_length=16, null=False, blank=False)

    def __str__(self):
        return f'{self.code}:{self.weather}'

    class Meta:
        verbose_name = '天候コード（公共用水域及び地下水の水質測定計画）'
        verbose_name_plural = '天候コード（公共用水域及び地下水の水質測定計画）'


class WATER_COLOR_CODE_PUBLIC(models.Model):

    code = models.CharField(primary_key=True,verbose_name='色相コード（公共用水域及び地下水の水質測定計画）',max_length=3)
    color = models.CharField(verbose_name='色相',max_length=24,null=False,blank=False)
    def __str__(self):
        return f'{self.code}:{self.color}'
    class Meta:
        verbose_name = '色相コード（公共用水域及び地下水の水質測定計画）'
        verbose_name_plural = '色相コード（公共用水域及び地下水の水質測定計画）'

class ODOR_CODE_PUBLIC(models.Model):
    code = models.CharField(primary_key=True,verbose_name='臭気コード（公共用水域及び地下水の水質測定計画）',max_length=3)
    odor = models.CharField(verbose_name='臭気',max_length=24,null=False,blank=False)
    def __str__(self):
        return f'{self.code}:{self.odor}'
    class Meta:
        verbose_name = '臭気コード（公共用水域及び地下水の水質測定計画）'
        verbose_name_plural = '臭気コード（公共用水域及び地下水の水質測定計画）'

class WATER_SYSTEM_CLASS_CODE_PUBLIC(models.Model):
    code = models.CharField(primary_key=True,verbose_name='区分コード（公共用水域及び地下水の水質測定計画）',max_length=1)
    classification = models.CharField(verbose_name='水系区分',max_length=16,null=False,blank=False)
    def __str__(self):
        return f'{self.code}:{self.classification}'
    class Meta:
        verbose_name = '区分コード（公共用水域及び地下水の水質測定計画）'
        verbose_name_plural = '区分コード（公共用水域及び地下水の水質測定計画）'

class SURVEY_CLASS_CODE_PUBLIC(models.Model):
    code = models.CharField(primary_key=True,verbose_name='調査区分コード（公共用水域及び地下水の水質測定計画）',max_length=1)
    classification = models.CharField(verbose_name='調査区分',max_length=24,null=False,blank=False)
    def __str__(self):
        return f'{self.code}:{self.classification}'
    class Meta:
        verbose_name = '調査区分コード（公共用水域及び地下水の水質測定計画）'
        verbose_name_plural = '調査区分コード（公共用水域及び地下水の水質測定計画）'

class WIND_DIRECTION_CODE_PUBLIC(models.Model):
    code = models.CharField(primary_key=True,verbose_name='風向コード（公共用水域及び地下水の水質測定計画）',max_length=3)
    wind_direction = models.CharField(verbose_name='風向',max_length=8,null=False,blank=False)
    def __str__(self):
        return f'{self.code}:{self.wind_direction}'
    class Meta:
        verbose_name = '風向コード（公共用水域及び地下水の水質測定計画）'
        verbose_name_plural = '風向コード（公共用水域及び地下水の水質測定計画）'

class FLOW_REGIME_CODE_PUBLIC(models.Model):
    code = models.CharField(primary_key=True,verbose_name='流況コード（公共用水域及び地下水の水質測定計画）',max_length=2)
    flow_regime = models.CharField(verbose_name='流況',max_length=48,null=False,blank=False)
    def __str__(self):
        return f'{self.code}:{self.flow_regime}'
    class Meta:
        verbose_name = '流況コード（公共用水域及び地下水の水質測定計画））'
        verbose_name_plural = '流況コード（公共用水域及び地下水の水質測定計画）'


