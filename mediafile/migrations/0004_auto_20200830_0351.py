# Generated by Django 3.1 on 2020-08-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediafile', '0003_auto_20200830_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='typeoffile',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='Type',
            field=models.IntegerField(choices=[(1, 'Image'), (2, 'pdf'), (3, 'Video')], null=True),
        ),
    ]
