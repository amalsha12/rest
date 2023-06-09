# Generated by Django 4.1.4 on 2023-04-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodday', models.CharField(max_length=25)),
                ('foodname', models.CharField(max_length=250)),
                ('foodimg', models.ImageField(upload_to='pics')),
                ('fooddesc', models.TextField()),
                ('images', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]
