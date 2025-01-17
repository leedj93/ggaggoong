# Generated by Django 3.2.8 on 2021-10-29 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_img', models.ImageField(blank=True, null=True, upload_to='content/image/')),
                ('title_name', models.CharField(max_length=100)),
                ('sub_title_name', models.CharField(max_length=100)),
                ('content_date', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('people_number', models.IntegerField()),
                ('age_min', models.IntegerField()),
                ('age_max', models.IntegerField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contents_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=500)),
                ('detail_img', models.ImageField(blank=True, null=True, upload_to='content/detail_image/')),
                ('contents_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.contents')),
            ],
        ),
    ]
