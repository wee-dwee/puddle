# Generated by Django 4.2.5 on 2023-09-20 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'ordering': ('name',), 'verbose_name_plural': 'items'},
        ),
    ]