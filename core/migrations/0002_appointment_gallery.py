# Generated by Django 2.2.6 on 2020-05-10 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('image1', models.ImageField(upload_to='gallery/')),
                ('image2', models.ImageField(upload_to='gallery/')),
                ('image3', models.ImageField(upload_to='gallery/')),
                ('image4', models.ImageField(upload_to='gallery/')),
                ('image5', models.ImageField(upload_to='gallery/')),
                ('image6', models.ImageField(upload_to='gallery/')),
                ('image7', models.ImageField(upload_to='gallery/')),
                ('image8', models.ImageField(upload_to='gallery/')),
                ('image9', models.ImageField(upload_to='gallery/')),
                ('image10', models.ImageField(upload_to='gallery/')),
                ('image11', models.ImageField(upload_to='gallery/')),
                ('image12', models.ImageField(upload_to='gallery/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('age', models.CharField(default='', max_length=2)),
                ('contact', models.CharField(default='', max_length=13)),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sex', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Gender')),
            ],
            options={
                'verbose_name_plural': 'Appointments',
                'ordering': ['-date'],
            },
        ),
    ]
