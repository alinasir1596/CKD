from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_risk_1', '0003_auto_20191009_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions_1',
            name='su',
            field=models.FloatField(choices=[(0, '0.0'), (1, '1.0'), (2, '2.0'), (3, '3.0'), (4, '4.0')], default=0),
        ),
    ]
