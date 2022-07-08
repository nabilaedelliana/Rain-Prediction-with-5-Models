from flask import Flask, request, jsonify

app = Flask(__name__)

nama = "Edel"

@app.route("/") # ini homepagenya atau end point
def hello_world():
    return f"<p>Hello, {nama}!</p>"

@app.route("/ganti", methods=['POST'])
def ganti_nama():
    global nama
    content = request.json
    nama = content['nama']
    response = jsonify(success=True, message='nama sudah diganti')
    return response
    
app.run(debug=True) # fungsinya adl supaya mudah nge-debugnya, jadi nanti di local server bisa nunjukkin error yang detail
