import os
from app import create_app, db

# Create application instance
config_name = os.getenv('FLASK_ENV', 'production')
app = create_app(config_name)

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
