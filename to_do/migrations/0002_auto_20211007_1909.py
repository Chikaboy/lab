# Generated by Django 3.2.8 on 2021-10-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(),
        ),
    ]
