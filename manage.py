#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pymongo import MongoClient



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'listando.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

client= MongoClient('mongodb://user:user@ac-zvbacnb-shard-00-02.n4s7ayo.mongodb.net:27017/?ssl=true&replicaSet=atlas-89iqf1-shard-0&authSource=admin&retryWrites=true&w=majority')
print(client.list_database_names())