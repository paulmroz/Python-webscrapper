# Generated by Django 2.1 on 2019-08-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20190821_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='type',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]