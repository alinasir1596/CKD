from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_risk_1', '0004_auto_20191009_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions_1',
            name='su',
            field=models.IntegerField(choices=[(0, '0.0'), (1, '1.0'), (2, '2.0'), (3, '3.0'), (4, '4.0')], default=0),
        ),
    ]