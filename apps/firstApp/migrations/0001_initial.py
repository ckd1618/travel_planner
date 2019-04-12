# Generated by Django 2.0.7 on 2018-07-24 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=255, null=True)),
                ('lastName', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]