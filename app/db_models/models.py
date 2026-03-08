from .. import db
from datetime import datetime, timezone




class Users(db.Model):
	__tablename__ = 'users'
    
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(250), nullable=False)
	name = db.Column(db.String(250), nullable=False)
	fullname = db.Column(db.String(250), nullable=False)
	email = db.Column(db.String(250), nullable=False)
	password = db.Column(db.Text, nullable=False)
	is_active = db.Column(db.Boolean, default=True)

	create_datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
	edit_datetime = db.Column(db.DateTime)
	remove_datetime = db.Column(db.DateTime)
    
	users_roles = db.relationship('UsersRoles', backref='user', lazy='dynamic')


	def __repr__(self):
		return f'<User -> id: {self.id}>'




class Roles(db.Model):
	__tablename__ = 'roles'
    
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	create_datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
	edit_datetime = db.Column(db.DateTime)
	remove_datetime = db.Column(db.DateTime)
    
	users_roles = db.relationship('UsersRoles', backref='role', lazy='dynamic')


	def __repr__(self):
		return f'<Role -> id: {self.id}>'




class UsersRoles(db.Model):
	__tablename__ = 'users_roles'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


	def __repr__(self):
		return f'<UserRole -> id: {self.id}>'