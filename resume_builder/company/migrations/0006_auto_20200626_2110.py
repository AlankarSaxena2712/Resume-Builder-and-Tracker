# Generated by Django 3.0.7 on 2020-06-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_company_coming_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_coming',
            name='branch_ce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company_coming',
            name='branch_ceit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company_coming',
            name='branch_cse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company_coming',
            name='branch_ec',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company_coming',
            name='branch_en',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company_coming',
            name='branch_it',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company_coming',
            name='branch_mba',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company_coming',
            name='branch_mca',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company_coming',
            name='branch_me',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='company_coming',
            name='students_applied',
        ),
        migrations.AddField(
            model_name='company_coming',
            name='students_applied',
            field=models.CharField(default='', max_length=1500),
            preserve_default=False,
        ),
    ]
