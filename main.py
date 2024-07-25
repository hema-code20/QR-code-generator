from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()
    data = request.form.get('link')

    if data:
        image = qrcode.make(data)
        image.save(memory, format='PNG')
        memory.seek(0)
        base64_image = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
    else:
        base64_image = None

    return render_template('index.html', data=base64_image)

if __name__ == '__main__':
    app.run(debug=True)
