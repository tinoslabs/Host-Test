# Generated by Django 3.1 on 2024-04-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinos_app', '0004_certificates'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_position', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('posted_date', models.DateField()),
                ('end_date', models.DateField()),
                ('post_end_date', models.DateTimeField()),
            ],
        ),
    ]
