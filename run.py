# /mnt/data/run.py

from database import init_db
from __init__ import app

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)

