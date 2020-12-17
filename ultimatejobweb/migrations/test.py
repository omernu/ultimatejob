from django.db import migrations, transaction
 
 
class Migration(migrations.Migration):
 
    dependencies = [
        ('ultimatejobweb', '0001_initial'),
    ]
 
    def generate_data(apps, schema_editor):
        from ultimatejobweb.models import user
        from django.contrib.auth.models import User
        from django.conf import settings
 
        user1 = User.objects.create_user("testuser1","last_name1","123456"),

        test_data = [
            ('DevOps', user1),
        ]
        
 
        with transaction.atomic():
            for profession, user_base in test_data:
               user_search = user(user=user_base, profession=profession)
               user_search.save()
 
    operations = [
       migrations.RunPython(generate_data),
    ]