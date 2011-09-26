from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from utils import build_file_name
import os
from config import app, db
from models import Igualito

@app.context_processor
def insertar_ultimos():
	ultimos = Igualito.query.all()[:5]
	return dict(ultimos=ultimos)

@app.route("/")
def index():
	igualitos = Igualito.query.all()[:5]
	return render_template('index.html', igualitos=igualitos )

@app.route("/upload/", methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		file1 = request.files['pic1']
		file2 = request.files['pic2']
		filename1 = build_file_name(file1.filename)
		filename2 = build_file_name(file2.filename)
		
		file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
		file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
		
		data = Igualito(request.form['name'], filename1, filename2)
		db.session.add(data)
		db.session.commit()
		
		return redirect(url_for('uploaded_end', file1=filename1, file2=filename2))
		
	return render_template('upload.html')
	
@app.route('/upload_end')
def uploaded_end():
	return render_template('uploaded_file.html')
	
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
	
@app.route('/show/')
@app.route("/show/<name>")
def post(name=None):
	return render_template('index.html', name=name)
	
@app.route("/get", methods=['POST'])
def obtener():
	pass

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
	

	
if __name__ == "__main__":
	app.debug = True
	app.run()