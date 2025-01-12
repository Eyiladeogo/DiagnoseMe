# Generated by Django 4.1.7 on 2023-05-07 15:44

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_alter_doctor_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[['Disease 1', 'Fungal infection'], ['Disease 2', 'Allergy'], ['Disease 3', 'GERD'], ['Disease 4', 'Chronic cholestasis'], ['Disease 5', 'Drug Reaction'], ['Disease 6', 'Peptic ulcer diseae'], ['Disease 7', 'AIDS'], ['Disease 8', 'Diabetes'], ['Disease 9', 'Gastroenteritis'], ['Disease 10', 'Bronchial Asthma'], ['Disease 11', 'Hypertension'], ['Disease 12', ' Migraine'], ['Disease 13', 'Cervical spondylosis'], ['Disease 14', 'Paralysis (brain hemorrhage)'], ['Disease 15', 'Jaundice'], ['Disease 16', 'Malaria'], ['Disease 17', 'Chicken pox'], ['Disease 18', 'Dengue'], ['Disease 19', 'Typhoid'], ['Disease 20', 'hepatitis A'], ['Disease 21', 'Hepatitis B'], ['Disease 22', 'Hepatitis C'], ['Disease 23', 'Hepatitis D'], ['Disease 24', 'Hepatitis E'], ['Disease 25', 'Alcoholic hepatitis'], ['Disease 26', 'Tuberculosis'], ['Disease 27', 'Common Cold'], ['Disease 28', 'Pneumonia'], ['Disease 29', 'Dimorphic hemmorhoids(piles)'], ['Disease 30', 'Heartattack'], ['Disease 31', 'Varicoseveins'], ['Disease 32', 'Hypothyroidism'], ['Disease 33', 'Hyperthyroidism'], ['Disease 34', 'Hypoglycemia'], ['Disease 35', 'Osteoarthristis'], ['Disease 36', 'Arthritis'], ['Disease 37', '(vertigo) Paroymsal  Positional Vertigo'], ['Disease 38', 'Acne'], ['Disease 39', 'Urinary tract infection'], ['Disease 40', 'Psoriasis'], ['Disease 41', 'Impetigo']], help_text='Category', max_length=1000),
        ),
    ]
