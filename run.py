from app import create_app
from app.models import db, User

app = create_app()

with app.app_context():
    db.create_all()

    admin_user = db.session.query(User).filter_by(username='admin').first()
    if not admin_user:
        admin = User(username='admin', role='admin')
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()
        print("The default admin has been successfully created with a hashed password")
    else:
        print("The database is ready to go")

if __name__ == '__main__':
    app.run()