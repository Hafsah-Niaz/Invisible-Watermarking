from flask import Flask, render_template, request, send_file
import os
from watermark import add_watermark, trace_watermark
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_watermark', methods=['POST'])
def add():
    file = request.files['file']
    text = request.form['text']
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    output_path = os.path.join(PROCESSED_FOLDER, f"wm_{filename}")
    add_watermark(path, text, output_path)

    return send_file(output_path, as_attachment=True)

@app.route('/trace', methods=['POST'])
def trace():
    file = request.files['file']
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    result = trace_watermark(path)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
