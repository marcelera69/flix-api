# Generated by Django 5.0.4 on 2024-05-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_alter_actor_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('US', 'Estados Unidos'), ('BR', 'Brasil'), ('FR', 'França'), ('DE', 'Alemnaha'), ('UK', 'Inglaterra'), ('IT', 'Italia'), ('ES', 'Espanha')], max_length=50, null=True),
        ),
    ]
