# Generated by Django 4.2 on 2023-05-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_c_exprience_contact_us_feedback_c_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='forget_password_token',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
