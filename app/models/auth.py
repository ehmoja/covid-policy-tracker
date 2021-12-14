from flask_sqlalchemy import SQLAlchemy


def get_user_cls(db: SQLAlchemy):
    class CustomerUser(db.Model):
        email = db.Column(db.String(254), primary_key=True)
        first_name = db.Column(db.String(40))
        last_name = db.Column(db.String(40))
        full_name = db.Column(db.String(70))
        tenant_id = db.Column(db.String(36))
        domain = db.Column(db.String(252))
    return CustomerUser
