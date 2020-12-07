# Generated by Django 3.0.7 on 2020-12-07 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ssp', '0003_auto_20201015_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='hash',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='link_set', to='ssp.hashed_value'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='location_set', to='ssp.address'),
        ),
        migrations.AlterField(
            model_name='system_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='system_user_set', to='ssp.person'),
        ),
    ]
