#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 'freinds_project.settings'
    )
    os.environ.setdefault('DJANGO_CONFIGURATION', 'ConfigClass')

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
