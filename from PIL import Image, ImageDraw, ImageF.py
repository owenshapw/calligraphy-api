from PIL import Image, ImageDraw, ImageFont

def generate_calligraphy(text, font_path='/Users/owen/Library/Fonts/FZYanZQKSJF.TTF', font_size=120):
    font = ImageFont.truetype(font_path, font_size)
    # 计算图像尺寸
    width = font_size * len(text)
    height = font_size * 2
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    for i, char in enumerate(text):
        draw.text((i * font_size, 0), char, font=font, fill='black')

    img.save("output_calligraphy.jpg")
    print("✅ 生成成功！")

# 示例调用
generate_calligraphy("厚德载物")