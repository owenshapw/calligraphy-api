from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import math

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    print("📥 收到请求啦！request.form:", request.form)

    text = request.form.get('text', '')
    layout = request.form.get('layout', 'horizontal')

    if not text:
        print("⚠️ 缺少 text 参数")
        return 'Missing text', 403

    import os
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'FZYanZQKSJF.TTF')
    if layout == 'vertical':
        font_size = 65  # 小一号，避免视觉太大
        row_spacing = 1.2
    else:
        font_size = 65
        row_spacing = 0.5

    font = ImageFont.truetype(font_path, font_size)

    if layout == 'vertical':
        # 竖排逻辑（每列 5 字）
        chars_per_col = 5
        col_width = font_size
        col_height = font_size * chars_per_col + 30
        num_cols = math.ceil(len(text) / chars_per_col)
        img_width = num_cols * col_width + 40
        img_height = col_height + 60

        img = Image.new('RGB', (img_width, img_height), color='white')
        draw = ImageDraw.Draw(img)

        for i, char in enumerate(text):
            col = i // chars_per_col
            row = i % chars_per_col
            x = img_width - (col + 1) * col_width - 20
            y = 5 + row * int(font_size * row_spacing)
            draw.text((x, y), char, font=font, fill='black')
    else:
        # 横排逻辑
        max_chars_per_line = 5
        line_height = int(font_size * 1.2)
        lines = [text[i:i+max_chars_per_line] for i in range(0, len(text), max_chars_per_line)]
        img_width = font_size * max_chars_per_line + 40
        img_height = line_height * len(lines) + 50

        img = Image.new('RGB', (img_width, img_height), color='white')
        draw = ImageDraw.Draw(img)

        for idx, line in enumerate(lines):
            draw.text((20, 20 + idx * line_height), line, font=font, fill='black')
 
    # 返回图片
    buffer = BytesIO()
    img.save(buffer, format='JPEG')
    buffer.seek(0)
    return send_file(buffer, mimetype='image/jpeg')

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))  # 本地默认 5001，云端自动替换
    app.run(host='0.0.0.0', port=port)
