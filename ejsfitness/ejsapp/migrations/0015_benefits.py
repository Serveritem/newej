# Generated by Django 4.2.4 on 2024-08-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejsapp', '0014_part'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('name2', models.CharField(max_length=250)),
                ('name3', models.CharField(max_length=250)),
                ('name4', models.CharField(max_length=250)),
                ('name5', models.CharField(max_length=250)),
                ('name6', models.CharField(max_length=250)),
                ('name7', models.CharField(max_length=250)),
                ('name8', models.CharField(max_length=250)),
                ('name9', models.CharField(max_length=250)),
                ('name10', models.CharField(max_length=250)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image9', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('image10', models.ImageField(blank=True, null=True, upload_to='benefits')),
                ('description1', models.TextField(max_length=250)),
                ('description2', models.TextField(max_length=250)),
                ('description3', models.TextField(max_length=250)),
                ('description4', models.TextField(max_length=250)),
                ('description5', models.TextField(max_length=250)),
                ('description6', models.TextField(max_length=250)),
                ('description7', models.TextField(max_length=250)),
                ('description8', models.TextField(max_length=250)),
                ('description9', models.TextField(max_length=250)),
                ('description10', models.TextField(max_length=250)),
            ],
        ),
    ]
