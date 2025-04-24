# main.py

from database import create_db
from interface import launch_app

if __name__ == "__main__":
    create_db()
    launch_app()
