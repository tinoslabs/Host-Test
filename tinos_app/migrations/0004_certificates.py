# Generated by Django 3.1 on 2024-04-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinos_app', '0003_delete_certificates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('join_date', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
