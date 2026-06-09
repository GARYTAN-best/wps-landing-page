#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
WIDTH = 1080
BG_COLOR = "#FFFFFF"
FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_BOLD_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"

# Load fonts
def load_font(size):
    return ImageFont.truetype(FONT_PATH, size)

def load_font_bold(size):
    return ImageFont.truetype(FONT_PATH, size)

# Create image
img = Image.new('RGB', (WIDTH, 2800), BG_COLOR)
draw = ImageDraw.Draw(img)

# Color palette
RED = "#D93025"
BLUE_DARK = "#1A5276"
BLUE_BG = "#EBF5FB"
BLUE_ICON = "#2E86C1"
GREEN_BG = "#D5F5E3"
GREEN_TEXT = "#1E8449"
ORANGE_DARK = "#7D6608"
ORANGE_BG = "#FEF9E7"
ORANGE_ICON = "#F39C12"
TEXT_DARK = "#2C3E50"
TEXT_GRAY = "#5D6D7E"
TEXT_LIGHT = "#85929E"

# Helper: draw wrapped text
def draw_wrapped_text(draw, text, x, y, font, max_width, fill, line_spacing=8):
    lines = []
    current_line = ""
    for char in text:
        test_line = current_line + char
        bbox = font.getbbox(test_line)
        if bbox[2] - bbox[0] > max_width:
            lines.append(current_line)
            current_line = char
        else:
            current_line = test_line
    if current_line:
        lines.append(current_line)

    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        bbox = font.getbbox(line)
        y += bbox[3] - bbox[1] + line_spacing
    return y

y = 60

# Title
font_title = load_font(42)
draw.text((WIDTH//2, y), "在线预览编辑能力-线上售卖", font=font_title, fill=RED, anchor="mt")
bbox = font_title.getbbox("在线预览编辑能力-线上售卖")
y += bbox[3] - bbox[1] + 60

# ========== Section 1: 按量计费 ==========
# Blue circle icon
circle_x = 70
circle_y = y + 20
draw.ellipse([circle_x - 25, circle_y - 25, circle_x + 25, circle_y + 25], fill=BLUE_ICON)
# Simple chart icon inside circle
draw.line([circle_x - 12, circle_y + 10, circle_x - 4, circle_y - 2], fill="white", width=2)
draw.line([circle_x - 4, circle_y - 2, circle_x + 4, circle_y + 2], fill="white", width=2)
draw.line([circle_x + 4, circle_y + 2, circle_x + 12, circle_y - 10], fill="white", width=2)

# Section title
font_section = load_font_bold(32)
title_text = "按量计费——按最大文档并发数阶梯计费"
draw.text((120, y), title_text, font=font_section, fill=BLUE_DARK)
bbox = font_section.getbbox(title_text)
y += bbox[3] - bbox[1] + 30

# Blue background area
section1_start = y
section1_end = y + 320

# Pricing tiers
font_body = load_font(24)
font_body_small = load_font(22)

# Draw pricing info
y_pricing = section1_start + 10

# Pricing tiers line
pricing_line = "1-20 并发——每次调用单价为 2.5 元；21-50 并发——单价 2.2 元；51-100 并发——单价 2 元"
y_pricing = draw_wrapped_text(draw, pricing_line, 120, y_pricing, font_body, WIDTH - 160, TEXT_DARK, line_spacing=10)

# Doc size info
y_pricing += 10
doc_line1 = "文档尺寸默认支持 100M"
y_pricing = draw_wrapped_text(draw, doc_line1, 120, y_pricing, font_body, WIDTH - 160, TEXT_DARK, line_spacing=10)

y_pricing += 10
doc_line2 = "每增加 100M 每月加收 300 元，上限 500M"
y_pricing = draw_wrapped_text(draw, doc_line2, 120, y_pricing, font_body, WIDTH - 160, TEXT_DARK, line_spacing=10)

# Green note box
y_pricing += 25
green_box_top = y_pricing - 15
green_box_bottom = y_pricing + 100
green_box_left = 120
green_box_right = WIDTH - 40
draw.rounded_rectangle([green_box_left, green_box_top, green_box_right, green_box_bottom], radius=8, fill=GREEN_BG)

font_note = load_font(20)
note_line1 = "最大并发文档数指用户通过应用同一时间点调用 WPS 服务打开不同文档的最大数量"
note_line2 = "每月基础套餐费：750 元/月，若月实际费用低于 750 元，按基础套餐费结算"
note_line3 = "若大于 750 元，按实际费用结算"

note_y = green_box_top + 18
draw_wrapped_text(draw, note_line1, green_box_left + 20, note_y, font_note, green_box_right - green_box_left - 40, GREEN_TEXT, line_spacing=6)
note_y += 35
draw_wrapped_text(draw, note_line2, green_box_left + 20, note_y, font_note, green_box_right - green_box_left - 40, GREEN_TEXT, line_spacing=6)
note_y += 35
draw_wrapped_text(draw, note_line3, green_box_left + 20, note_y, font_note, green_box_right - green_box_left - 40, GREEN_TEXT, line_spacing=6)

y = green_box_bottom + 50

# ========== Section 2: 套餐计费 ==========
# Orange circle icon
circle_y2 = y + 20
draw.ellipse([circle_x - 25, circle_y2 - 25, circle_x + 25, circle_y2 + 25], fill=ORANGE_ICON)
# Simple package icon inside circle
draw.rectangle([circle_x - 12, circle_y2 - 8, circle_x + 12, circle_y2 + 12], fill="white")
draw.line([circle_x - 12, circle_y2 - 2, circle_x + 12, circle_y2 - 2], fill=ORANGE_ICON, width=1)

# Section title
title_text2 = "套餐计费"
draw.text((120, y), title_text2, font=font_section, fill=ORANGE_DARK)
bbox2 = font_section.getbbox(title_text2)
y += bbox2[3] - bbox2[1] + 15

# Subtitle
font_sub = load_font(22)
sub_text = "按年收费，分为三个梯度 (18000, 25920, 41760):"
draw.text((120, y), sub_text, font=font_sub, fill=TEXT_GRAY)
bbox3 = font_sub.getbbox(sub_text)
y += bbox3[3] - bbox3[1] + 30

# Package cards
font_card_title = load_font_bold(22)
font_card_body = load_font(20)

packages = [
    {
        "title": "在线预览编辑能力 (50并发)",
        "price": "18000",
        "features": [
            "① 单文档并发数50",
            "② 文档大小支持100M",
            "③ 支持PDF/Office文档转换",
            "④ 支持文档在线查看",
            "⑤ 支持文档在线编辑"
        ]
    },
    {
        "title": "在线预览编辑能力 (100并发)",
        "price": "25920",
        "features": [
            " 单文档并发数100",
            "② 文档大小支持100M",
            "③ 支持PDF/Office文档转换",
            "④ 支持文档在线查看",
            "⑤ 支持文档在线编辑",
            "⑥ 支持多人协同编辑"
        ]
    },
    {
        "title": "在线预览编辑能力 (500并发)",
        "price": "41760",
        "features": [
            "① 单文档并发数500",
            "② 文档大小支持100M",
            "③ 支持PDF/Office文档转换",
            "④ 支持文档在线查看",
            "⑤ 支持文档在线编辑",
            "⑥ 支持多人协同编辑",
            "⑦ 支持自定义域名"
        ]
    }
]

card_padding = 20
card_width = WIDTH - 80
card_height = 420
card_gap = 20

for i, pkg in enumerate(packages):
    card_y = y + i * (card_height + card_gap)

    # Draw card background
    draw.rounded_rectangle([40, card_y, WIDTH - 40, card_y + card_height], radius=12, fill="#F8F9FA", outline="#E0E0E0", width=1)

    # Card title
    draw.text((60, card_y + 15), pkg["title"], font=font_card_title, fill=TEXT_DARK)

    # Price
    font_price = load_font_bold(36)
    price_text = pkg["price"] + " 元/年"
    draw.text((60, card_y + 55), price_text, font=font_price, fill="#E74C3C")

    # Features
    feature_y = card_y + 110
    for feature in pkg["features"]:
        draw.text((60, feature_y), feature, font=font_card_body, fill=TEXT_GRAY)
        bbox_f = font_card_body.getbbox(feature)
        feature_y += bbox_f[3] - bbox_f[1] + 12

y = y + 3 * (card_height + card_gap) + 40

# ========== Bottom note ==========
font_bottom = load_font(20)
bottom_text1 = "WPS 365商业高级版及以上可以优惠价格增购套餐 (16200, 23300, 37500)"
bottom_text2 = "具体见套餐权益流程可参考文档"

draw.text((WIDTH//2, y), bottom_text1, font=font_bottom, fill=BLUE_DARK, anchor="mt")
bbox_b1 = font_bottom.getbbox(bottom_text1)
y += bbox_b1[3] - bbox_b1[1] + 10
draw.text((WIDTH//2, y), bottom_text2, font=font_bottom, fill=BLUE_DARK, anchor="mt")

# Crop to actual content height
actual_height = y + 60
img = img.crop((0, 0, WIDTH, actual_height))

# Save
output_path = "/Users/garytan/Downloads/截屏2026-06-09 14.28.23_竖版.png"
img.save(output_path, "PNG", quality=95)
print(f"Saved to: {output_path}")
print(f"Size: {img.size}")
