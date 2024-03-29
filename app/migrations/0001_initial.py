# Generated by Django 4.1.7 on 2023-12-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Punjab', 'Punjab'), ('Sindh', 'Sindh'), ('Khyber Pakhtunkhwa', 'Khyber Pakhtunkhwa'), ('Balochistan', 'Balochistan'), ('Gilgit-Baltistan', 'Gilgit-Baltistan'), ('Azad Jammu and Kashmir', 'Azad Jammu and Kashmir'), ('Islamabad Capital Territory', 'Islamabad Capital Territory')], max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile')),
                ('file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
