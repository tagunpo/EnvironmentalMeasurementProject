# Generated by Django 4.2.7 on 2023-11-21 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TecrisClassCode',
            fields=[
                ('tecris_class_code', models.CharField(max_length=1, primary_key=True, serialize=False, verbose_name='テクリス区分コード')),
                ('tecris_class_name', models.CharField(max_length=8, verbose_name='区分')),
            ],
            options={
                'verbose_name': 'テクリス区分コード',
                'verbose_name_plural': 'テクリス区分コード',
            },
        ),
        migrations.CreateModel(
            name='TecrisRiverTypeCode',
            fields=[
                ('tecris_river_type_code', models.CharField(max_length=1, primary_key=True, serialize=False, verbose_name='テクリス河川種類コード')),
                ('tecris_water_system_class', models.CharField(max_length=16, verbose_name='水系区分')),
                ('tecris_river_type', models.CharField(max_length=16, verbose_name='河川種類')),
            ],
            options={
                'verbose_name': 'テクリス河川種類コード',
                'verbose_name_plural': 'テクリス河川種類コード',
            },
        ),
        migrations.CreateModel(
            name='TecrisWaterSystemCode',
            fields=[
                ('tecris_water_system_code', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='テクリス一級水系番号')),
                ('tecris_water_system', models.CharField(max_length=16, verbose_name='水系名')),
                ('tecris_class_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TecrisDB.tecrisclasscode', verbose_name='テクリス区分コード')),
                ('tecris_river_type_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TecrisDB.tecrisrivertypecode', verbose_name='テクリス河川種類コード')),
            ],
            options={
                'verbose_name': 'テクリス水系コード',
                'verbose_name_plural': 'テクリス水系コード',
            },
        ),
    ]
