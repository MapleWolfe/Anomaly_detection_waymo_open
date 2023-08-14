from flask import Flask, render_template, request, session, flash
import os
from werkzeug.utils import secure_filename

#*** Backend operation
 
# WSGI Application
# Defining upload folder path
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
 
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name for template path
# The default folder name for static files should be "static" else need to mention custom folder for static path
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
# Configure upload folder for Flask application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
# Define secret key to enable session
app.secret_key = 'This is your secret key to utilize session in Flask'
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

 
@app.route('/')
def index():
    return render_template('upload_display.html')
 

@app.route('/',  methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        # Upload file flask
        uploaded_img = request.files['uploaded-file']
        # Extracting uploaded data file name
        img_filename = secure_filename(uploaded_img.filename)
        # Upload file to database (defined uploaded folder in static path)
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        # Storing uploaded file path in flask session
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
        img_file_path = session.get('uploaded_img_file_path', None)
        return render_template('upload_display_2.html', user_image = img_file_path)

# this is for displaying the segmentation result 
@app.route('/show_seg')
def display_segmentation():
    # Retrieving uploaded file path from session
    img_segmentation_path = os.path.join(app.config['UPLOAD_FOLDER'], 'seg1.png')
    # Display image in Flask application web page
    return render_template('show_image_seg.html', user_image = img_segmentation_path)

# this is for displaying the detection result 
@app.route('/show_dectect')
def display_dectection():
    # Retrieving uploaded file path from session
    img_detection_path = os.path.join(app.config['UPLOAD_FOLDER'], 'detected.png')
    # Display image in Flask application web page
    return render_template('show_image_detection.html', user_image = img_detection_path)


if __name__=='__main__':
    app.run(debug = True)