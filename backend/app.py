from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Route to render the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle map uploads
@app.route('/upload_map', methods=['POST'])
def upload_map():
    if 'map' in request.files:
        map_file = request.files['map']
        map_file.save(os.path.join('static/maps/', map_file.filename))
        return render_template('index.html', map=map_file.filename)

if __name__ == '__main__':
    app.run(debug=True)
