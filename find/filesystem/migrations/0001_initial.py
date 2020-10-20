# Generated by Django 3.1.2 on 2020-10-19 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startdir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_path', models.CharField(default='.', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=18)),
                ('file_path', models.CharField(max_length=255)),
                ('relative_to_startdir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filesystem.startdir')),
            ],
        ),
    ]