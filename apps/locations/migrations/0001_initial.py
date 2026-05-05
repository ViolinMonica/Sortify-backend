from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('facility_type', models.CharField(choices=[('BANK_SAMPAH', 'Waste Bank'), ('TPS', 'Temporary Waste Disposal Site'), ('TPS_ORGANIK', 'Organic Waste Disposal Site'), ('PENGEPUL_LOGAM', 'Scrap Metal Collector'), ('TPA', 'Final Waste Disposal Site')], max_length=20)),
                ('city', models.CharField(db_index=True, max_length=100)),
                ('province', models.CharField(default='', max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('maps_url', models.URLField(blank=True, default='')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['city', 'name'],
            },
        ),
    ]