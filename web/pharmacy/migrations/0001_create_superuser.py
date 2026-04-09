import logging

from django.conf import settings
from django.db import migrations

logger = logging.getLogger(__name__)


def create_development_superuser(apps, schema_editor):
    from django.contrib.auth.models import User

    if settings.AUTH_SUPERUSER_EMAIL and settings.AUTH_SUPERUSER_PASSWORD:
        superuser = User.objects.create_superuser(
            username=settings.AUTH_SUPERUSER_EMAIL,
            email=settings.AUTH_SUPERUSER_EMAIL,
            password=settings.AUTH_SUPERUSER_PASSWORD,
            first_name="Admin",
        )
        logger.info("Superuser '{superuser}' created.".format(superuser=superuser))
    else:
        logger.info("Superuser not created.")


def delete_development_superuser(apps, schema_editor):
    from django.contrib.auth.models import User

    superuser = User.objects.filter(email=settings.AUTH_SUPERUSER_EMAIL).first()
    if superuser:
        superuser.delete()
        logger.info("Superuser '{superuser}' deleted.".format(superuser=superuser))
    else:
        logger.info("Superuser not found; did not delete.")


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(
            create_development_superuser,
            reverse_code=delete_development_superuser,
        ),
    ]
