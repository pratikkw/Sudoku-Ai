from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def clear_upload_folder():
  for filename in os.listdir(UPLOAD_FOLDER):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if(os.path.isfile(file_path)):
      os.remove(file_path)


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload_file():
  if 'file' not in request.files:
    return jsonify({"error": "No file uploaded", 'status' : 400}), 400
  
  file = request.files['file']
  if(file.filename == ""):
    return jsonify({"error": "No file selected", 'status' : 400}), 400
  
  clear_upload_folder()
  name, ext = file.filename.split('.')
  file_path = os.path.join(UPLOAD_FOLDER, f'users_sudoku.{ext}')
  file.save(file_path)

  return jsonify({"message": "File uploaded successfully", 'status' : 200, "file_path": f"users_sudoku.{ext}"})


if(__name__ == "__main__"):
  app.run(debug=True)