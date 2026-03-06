from .. import db
# from datetime import datetime, timezone




class ModelName(db.Model):
	__tablename__ = 'table_name'
    
	id = db.Column(db.Integer, primary_key=True)
	string_field = db.Column(db.String(250), nullable=False)
    
	rel_ship = db.relationship('ModelName2', backref='table_name', lazy='dynamic')


	def __repr__(self):
		return f'<ModelName -> id: {self.id}>'


class ModelName2(db.Model):
	__tablename__ = 'table_name_2'

	id = db.Column(db.Integer, primary_key=True)
	table_name_id = db.Column(db.Integer, db.ForeignKey('table_name.id'))

	string_field = db.Column(db.String(250), nullable=False)


	def __repr__(self):
		return f'<ModelName2 -> id: {self.id}>'