# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 03:51


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileBrowserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(choices=[('img', 'Image'), ('doc', 'Document')], max_length=3)),
                ('uploaded_file', models.FileField(upload_to='mce_filebrowser/%Y/%m/%d', verbose_name='File / Image')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
            ],
        ),
    ]
