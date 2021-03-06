# Generated by Django 3.1 on 2020-08-16 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediafile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('mediafile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediafile.uploadfile')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
