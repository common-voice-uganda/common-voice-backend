# Generated by Django 2.2 on 2019-04-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonvoice', '0002_auto_20190414_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='common_voice_id',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='recording',
            name='verify_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recording',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
