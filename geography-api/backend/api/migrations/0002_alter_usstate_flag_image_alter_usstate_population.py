# Generated by Django 4.0.3 on 2022-03-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usstate',
            name='flag_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='usstate',
            name='population',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
