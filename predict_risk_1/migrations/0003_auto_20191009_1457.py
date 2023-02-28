from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_risk_1', '0002_auto_20191009_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions_1',
            name='bgr',
            field=models.FloatField(default=89),
        ),
        migrations.AlterField(
            model_name='predictions_1',
            name='hemo',
            field=models.FloatField(default=15),
        ),
        migrations.AlterField(
            model_name='predictions_1',
            name='pot',
            field=models.FloatField(default=5),
        ),
        migrations.AlterField(
            model_name='predictions_1',
            name='rc',
            field=models.FloatField(default=5),
        ),
        migrations.AlterField(
            model_name='predictions_1',
            name='sc',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='predictions_1',
            name='sod',
            field=models.FloatField(default=144),
        ),
    ]