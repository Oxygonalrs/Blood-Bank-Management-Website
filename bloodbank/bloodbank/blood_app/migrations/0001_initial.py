# Generated by Django 2.2 on 2020-05-14 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserExtend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(help_text='yyyy-mm-dd')),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=10)),
                ('ready_to_donate', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='images/', verbose_name='Profile Picture')),
                ('last_donate', models.DateField()),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood_app.BloodGroup')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood_app.District')),
                ('donor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestBlood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('donation_location', models.CharField(max_length=100)),
                ('date_of_donation', models.DateField()),
                ('pin_code', models.IntegerField(help_text='You can edit request later using this code', unique=True)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood_app.BloodGroup')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood_app.District')),
            ],
        ),
    ]
