# Generated by Django 3.1.4 on 2021-01-08 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0003_auto_20210107_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='system_control',
            name='control_primary_system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ssp.system_security_plan'),
        ),
    ]
