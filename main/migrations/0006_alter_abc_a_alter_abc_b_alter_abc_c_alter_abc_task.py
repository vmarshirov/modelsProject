# Generated by Django 4.0.4 on 2023-02-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_abc_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abc',
            name='a',
            field=models.IntegerField(default=0, verbose_name='Значение А'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='b',
            field=models.IntegerField(default=0, verbose_name='Значение B'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='c',
            field=models.IntegerField(default=0, verbose_name='Значение С'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='task',
            field=models.CharField(default='Равна ли С сумме A и B ?', max_length=256, verbose_name='Формулировка задачи'),
        ),
    ]
