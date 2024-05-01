# Generated by Django 5.0.4 on 2024-05-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil'), ('FRANCE', 'França'), ('GERMANY', 'Alemnaha'), ('UK', 'Inglaterra'), ('IT', 'Italia'), ('ES', 'Espanha')], max_length=50, null=True),
        ),
    ]
