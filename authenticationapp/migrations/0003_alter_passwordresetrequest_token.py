# Generated by Django 5.1.4 on 2025-01-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationapp', '0002_alter_passwordresetrequest_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='7MY8eQ2myWzJlsVqoeWC3vAp2xMPsX2E', editable=False, max_length=32, unique=True),
        ),
    ]
