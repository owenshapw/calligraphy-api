#!/usr/bin/env python3

# 字体映射字典
FONT_MAPPING = {
    'yan': 'FZYanZQKSJF.TTF',  # 颜体
    'wen': 'FZWenZMXKJW.TTF',  # 文征明体
    'zhao': 'FZZCHJW.TTF',     # 赵体
    'zheng': 'FZZJ-HFHWJW.TTF', # 郑体
    'alibaba': 'AlibabaHealthFont20CN-45R.TTF',  # 阿里巴巴体
    'qigong': 'FZQiGXKJF.TTF',  # 启功体
    'qigong_w': 'FZQiGXKJW.TTF',  # 启功体(文)
    'zhao_js': 'FZZhaoJSJSJF.TTF',  # 赵体(简体)
    'wang_xz': 'FZWangXZXSJF.TTF',  # 王羲之体
    'liu_gq': 'FZLiuGQKSJF.TTF',  # 柳公权体
    'sj_yis': 'FZSJ-YISQXSPZ.TTF',  # 宋体(艺术)
    'liu_bs': 'FZLiuBSLSJW.TTF',  # 刘炳森体
    'zhao_js_w': 'FZZhaoJSJSJW.TTF',  # 赵体(简体文)
    'yi_yl': 'FZYiYBLSJW.TTF',  # 易英体
    'sha': '沙氏体.ttf'
}

import os

# 测试沙氏体映射
font_style = 'sha'
font_filename = FONT_MAPPING.get(font_style, 'FZYanZQKSJF.TTF')
font_path = os.path.join('fonts', font_filename)

print(f"🎨 选择的字体: {font_style} -> {font_filename}")
print(f"📁 字体路径: {font_path}")
print(f"✅ 字体文件存在: {os.path.exists(font_path)}")

# 测试所有字体文件是否存在
print("\n📋 检查所有字体文件:")
for key, filename in FONT_MAPPING.items():
    path = os.path.join('fonts', filename)
    exists = os.path.exists(path)
    print(f"  {key}: {filename} -> {'✅' if exists else '❌'}") 