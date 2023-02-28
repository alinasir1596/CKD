from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=33)),
                ('bp', models.IntegerField(default=80)),
                ('sg', models.IntegerField(default=1)),
                ('al', models.IntegerField(choices=[(0, '0.0'), (1, '1.0'), (2, '2.0'), (3, '3.0'), (4, '4.0')], default=0)),
                ('su', models.IntegerField(choices=[(0, '0.0'), (1, '1.0'), (2, '2.0'), (3, '3.0'), (4, '4.0')], default=0)),
                ('rbc', models.IntegerField(choices=[(1, 'normal'), (0, 'abnormal')], default=1)),
                ('pc', models.IntegerField(choices=[(1, 'normal'), (0, 'abnormal')], default=1)),
                ('pcc', models.IntegerField(choices=[(1, 'present'), (0, 'notpresent')], default=0)),
                ('ba', models.IntegerField(choices=[(1, 'present'), (0, 'notpresent')], default=0)),
                ('bgr', models.IntegerField(default=89)),
                ('bu', models.IntegerField(default=19)),
                ('sc', models.IntegerField(default=1)),
                ('sod', models.IntegerField(default=144)),
                ('pot', models.IntegerField(default=5)),
                ('hemo', models.IntegerField(default=15)),
                ('pcv', models.IntegerField(default=40)),
                ('wc', models.IntegerField(default=10300)),
                ('rc', models.IntegerField(default=5)),
                ('htn', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('dm', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('cad', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('appet', models.IntegerField(choices=[(1, 'good'), (0, 'poor')], default=1)),
                ('pe', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('ane', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('predicted_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('classification', models.IntegerField(choices=[(1, 'ckd'), (0, 'nockd')], default=1)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predict_1', to='accounts.UserProfileInfo')),
            ],
        ),
    ]
