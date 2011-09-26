from config import db

class Igualito(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	file1 = db.Column(db.String(200), unique=True)
	file2 = db.Column(db.String(200), unique=True)
	name = db.Column(db.String(150), unique=False)
	
	def __init__(self, name, file1, file2):
		self.name = name
		self.file1 = file1
		self.file2 = file2
		
	def __repr__(self):
		return '<Igualito %r>' % self.name