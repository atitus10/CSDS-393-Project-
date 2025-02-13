# Generated by Django 3.2 on 2021-05-04 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_reservationslot_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='website.restaurant'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='restaurant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='website.restaurant'),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(default=0)),
                ('restaurant', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='website.restaurant')),
            ],
        ),
    ]
