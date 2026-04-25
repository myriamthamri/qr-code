from flask import Flask, render_template, request, jsonify
import qrcode
import base64
from io import BytesIO


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('qrcode.html')


@app.route('/generate', methods=['POST'])
def generate():
    """Receives URL and returns base64 QR image"""
    data = request.get_json()
    url = data.get('url', 'https://www.google.com/').strip()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format='PNG')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return jsonify({
        'image': f'data:image/png;base64,{img_base64}',
        'url': url
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)