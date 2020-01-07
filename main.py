from flask import Flask, redirect, url_for, request,render_template
from werkzeug import secure_filename
import tagging
app = Flask(__name__)

@app.route('/')
def upload_file():
	return render_template("upload1.html")	
@app.route('/uploader',methods =['POST','GET'])
def pos_tagging():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		result=tagging.main_program(f.filename)
		print(result)
		return result
		
app.debug = True
app.run(host= '0.0.0.0',port=5007)
