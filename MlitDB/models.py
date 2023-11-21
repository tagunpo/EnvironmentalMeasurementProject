from django.db import models
from TecrisDB.models import TECRIS_WATER_SYSTEM_CODE
# from DamDB.models import Coordinates
# Create your models here.

#河川コード
class WATER_SYSTEM_AREA_NO(models.Model):
    """水系域の地域番号　一級水系（地方整備局）　一級以外（都道府県）"""
    area_no = models.CharField(primary_key=True,verbose_name='水域系地域番号',max_length=2,null=False,blank=False)
    area_name = models.CharField(verbose_name='主管区分・都道府県',max_length=16,null=False,blank=False)
    def __str__(self):
        return f'{self.area_no}:{self.area_name}'

    class Meta:
        verbose_name = '水域系地域番号'
        verbose_name_plural = '水域系地域番号'

class WATER_SYSTEM(models.Model):
    """水系域コードテーブル"""
    water_system_code = models.CharField(primary_key=True,verbose_name='水系域コード',max_length=6,null=False,blank=False)
    water_system_name = models.CharField(verbose_name='水系名',max_length=64,null=False,blank=False)
    water_system_kana = models.CharField(verbose_name='読み仮名',max_length=64,null=True,blank=True)
    water_system_area_no = models.ForeignKey(WATER_SYSTEM_AREA_NO, verbose_name='地域番号', on_delete=models.SET_NULL,null=True,blank=True)
    water_system_no = models.CharField(verbose_name='水系番号',max_length=4,null=False,blank=False)
    # water_system_no_tecris = models.ForeignKey(TECRIS_WATER_SYSTEM_CODE,verbose_name='テクリス水系番号',related_name='TecrisDB', on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f'水域系コード:{self.water_system_code} 水域名:{self.water_system_name}'
        # return self.water_system_name
    class Meta:
        verbose_name = '水系域'
        verbose_name_plural = '水系域'

class RIVER(models.Model):
    """河川コード"""
    # river_type_choices = (
    #     ("1", "一級"), ("2", "二級"), ("3", "準用"), ("4", "普通"),
    # )
    river_code = models.CharField(primary_key=True,verbose_name='河川コード', max_length=10,null=False,blank=False)
    water_system = models.ForeignKey(WATER_SYSTEM, verbose_name='水系', on_delete=models.SET_NULL,null=True,blank=True)
    river_name = models.CharField(verbose_name='河川名', max_length=64, null=False, blank=False)
    river_kana = models.CharField(verbose_name='読み仮名', max_length=64, null=True, blank=True)
    stream_order = models.SmallIntegerField(verbose_name='次数', null=True, blank=True)
    river_type = models.CharField(verbose_name='河川種別', max_length=4, null=True, blank=True)
    river_administrator = models.CharField(verbose_name='河川管理者', max_length=16, null=True, blank=True)
    estuary_prefectures = models.CharField(verbose_name='河口都道府県名', max_length=16, null=True, blank=True)

    def __str__(self):
        # return f'河川コード:{self.river_code} 水系名:{self.water_system} 河川名:{self.river_name}'
        return f'河川コード:{self.river_code}  河川名:{self.river_name}'

        # return self.river_code

    class Meta:
        verbose_name = '河川'
        verbose_name_plural = '河川'

class DamCoordinates(models.Model):
    """地点座標テーブル"""
    coord_type_choices = (
        ("1","Tokyo"),("2","JGD2000"),("3","JGD2011"),("4","WGS1984"),
    )

    coord_type = models.CharField(verbose_name='座標系',max_length=7,choices=coord_type_choices)
    lat = models.FloatField(verbose_name='緯度',null=True,blank=True)
    lon = models.FloatField(verbose_name='経度', null=True, blank=True)

    def __str__(self):
        return f'緯度:{self.lat:.6f} 経度:{self.lon:.6f} ({self.coord_type})'

    class Meta:
        verbose_name = 'ダム地点座標'
        verbose_name_plural = 'ダム地点座標'

class DamAttributePlus(models.Model):
    dam_type_code_choices = (
        ("1","アーチダム"),("2","バットレスダム"),("3","アースダム"),("4","アスファルトフェイシングダム"),("5","アスファルトコアダム"),
        ("6", "フローティングゲートダム（可動堰）"),("7", "重力式コンクリートダム"),("8", "重力式アーチダム"),
        ("9", "重力式コンクリートダム・フィルダム複合ダム"),("10", "中空重力式コンクリートダム"),
    )
    dam_purpose_code_choices = (
        ("1", "洪水調節、農地防災"), ("2", "不特定用水、河川維持用水"), ("3", "灌漑、特定(新規)灌漑用水"),("4", "上水道用水"),
        ("5", "工業用水道用水"),("6", "発電"), ("7", "消流雪用水"), ("8", "レクリエーション"),

    )
    # dam_code = models.CharField(primary_key=True,verbose_name='ダムコード', max_length=14,null=False,blank=False)
    # """ダム付加属性"""経度
    # dam_attribute_plus_1 = models.CharField(verbose_name='形式',max_length=128,null=True,blank=True)
    # dam_attribute_plus_2 = models.FloatField(verbose_name='集水面積（km2）', null=True, blank=True)
    # dam_attribute_plus_3 = models.FloatField(verbose_name='間接流域（外数値）', null=True, blank=True)
    # dam_attribute_plus_4 = models.FloatField(verbose_name='堤高（m）', null=True, blank=True)
    # dam_attribute_plus_5 = models.FloatField(verbose_name='堤長（m）', null=True, blank=True)
    # dam_attribute_plus_6 = models.FloatField(verbose_name='面積', null=True, blank=True)
    # dam_attribute_plus_7 = models.FloatField(verbose_name='堤体積', null=True, blank=True)
    # dam_attribute_plus_8 = models.FloatField(verbose_name='堤体積(コンクリート)（千m3）', null=True, blank=True)
    # dam_attribute_plus_9 = models.FloatField(verbose_name='堤体積(ロック)（千m3）', null=True, blank=True)
    # dam_attribute_plus_10 = models.FloatField(verbose_name='堤体積(アース)（千m3）', null=True, blank=True)


    # dam_purpose_code = models.CharField(verbose_name='ダム目的', max_length=64, choices=dam_purpose_code_choices)

    def __str__(self):
        return self.dam_code

    class Meta:
        verbose_name = 'ダム付加属性'
        verbose_name_plural = 'ダム付加属性'
class Dam(models.Model):
    """ダム"""
    dam_code = models.CharField(primary_key=True,verbose_name='ダムコード', max_length=14)
    dam_name = models.CharField(verbose_name='ダム名',max_length=32,null=False,blank=False)
    dam_administrator = models.CharField(verbose_name='ダム管理者', max_length=24, null=True, blank=True)
    dam_prefectures = models.CharField(verbose_name='都道府県名', max_length=8, null=True, blank=True)
    river = models.ForeignKey(RIVER,verbose_name='河川',related_name='Mlit_River',on_delete=models.SET_NULL,null=True,blank=True)
    # water_system_code = models.CharField(verbose_name='水域系コード', max_length=6, null=True, blank=True)
    # water_system_name = models.CharField(verbose_name='水域名', max_length=64, null=True, blank=True)
    # river_code = models.CharField(verbose_name='河川コード', max_length=10, null=True, blank=True)
    # river_name = models.CharField(verbose_name='河川名', max_length=64, null=True, blank=True)
    dam_coordinates = models.ForeignKey(DamCoordinates,verbose_name='位置',on_delete=models.CASCADE,null=True,blank=True)
    dam_attribute_plus = models.ForeignKey(DamAttributePlus,verbose_name='付加情報',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f'ダムコード:{self.dam_code} ダム名:{self.dam_name} ダム管理者:{self.dam_administrator}'
        # return f'ダムコード:{self.dam_code} '
    class Meta:
        verbose_name = 'ダム'
        verbose_name_plural = 'ダム'


