# Generated by Django 2.2 on 2020-12-18 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('message', models.TextField(blank=True)),
                ('video', models.CharField(blank=True, max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='hg_app.User')),
            ],
        ),
    ]
