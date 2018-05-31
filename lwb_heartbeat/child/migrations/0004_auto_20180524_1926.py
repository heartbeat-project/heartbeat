# Generated by Django 2.0.5 on 2018-05-24 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0003_auto_20180524_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'verbose_name_plural': 'Children'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'Education Programs'},
        ),
        migrations.AlterModelOptions(
            name='fostercare',
            options={'verbose_name_plural': 'Foster Care Programs'},
        ),
        migrations.AlterModelOptions(
            name='generalupdate',
            options={'verbose_name_plural': 'General Updates'},
        ),
        migrations.AlterModelOptions(
            name='growthdata',
            options={'verbose_name_plural': 'Growth Data'},
        ),
        migrations.AlterModelOptions(
            name='healinghome',
            options={'verbose_name_plural': 'Healing Home Programs'},
        ),
        migrations.AlterModelOptions(
            name='lwbprogram',
            options={'verbose_name_plural': 'LWB Programs'},
        ),
        migrations.AlterModelOptions(
            name='medical',
            options={'verbose_name_plural': 'Medical Programs'},
        ),
        migrations.AlterModelOptions(
            name='medicalcodes',
            options={'verbose_name_plural': 'Medical Codes'},
        ),
        migrations.AlterModelOptions(
            name='medicalupdate',
            options={'verbose_name_plural': 'Medical Updates'},
        ),
        migrations.AlterModelOptions(
            name='nutrition',
            options={'verbose_name_plural': 'Nutrition Programs'},
        ),
        migrations.AlterModelOptions(
            name='trafficking',
            options={'verbose_name_plural': 'Trafficking Programs'},
        ),
    ]