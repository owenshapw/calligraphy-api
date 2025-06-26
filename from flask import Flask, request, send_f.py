from flask import Flask, request, send_file
from your_script import generate_calligraphy  # 你上一步写的代码

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get("text", "")
    generate_calligraphy(text)
    return send_file("output_calligraphy.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)