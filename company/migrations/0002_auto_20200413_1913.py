# Generated by Django 3.0.5 on 2020-04-13 16:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'О компании'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='main',
            options={'verbose_name_plural': 'Главная'},
        ),
        migrations.AlterField(
            model_name='main',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
