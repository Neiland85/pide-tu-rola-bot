# /mnt/data/run.py

from database import init_db, app

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

