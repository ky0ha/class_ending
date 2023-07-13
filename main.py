from PIL import ImageFont, ImageDraw, Image
import argparse, json, time

parser = argparse.ArgumentParser(
    prog="Complex Pic",
    description="生成结课通知单"
)
parser.add_argument("-n", "--name", default=None, type=str, help="学生姓名")
parser.add_argument("-c", "--cname", default=None, type=str, help="所在班级：周x xx:xx")
parser.add_argument("-d", "--date", default=None, type=str, help="截止日期")
parser.add_argument("-t", "--teacher", default=None, type=str, help="老师名字")
args = parser.parse_args()
# test command: python main.py -n "陈思宇" -c "周日 14:45" -d "2023-7-13" -t "ky0ha"


class Date():
    def __init__(self, date):
        self.year, self.month, self.day = date.split('-')

print("---------start-----------")

# 获取参数
sname = args.name
cname = args.cname
date = Date(args.date)
tname = args.teacher
bk_img_path = r"结课通知单.jpg"
current_time = Date(time.strftime("%Y-%m-%d"))

# 图片路径
bk_img = Image.open(bk_img_path)

#设置需要显示的字体
fontpath = "font/simsun.ttc"    
draw = ImageDraw.Draw(bk_img)

# c = "周日 14:45 code4"
# font_size = 50
# while True:
#     print("***")
#     font = ImageFont.truetype(fontpath, font_size)
    
#     if draw.textlength(c, font=font) <= 255:
#         break
    
#     font_size -= 1

# 绘制文字信息   
# # (100,300/350)为字体的位置，(255,255,255)为白色，(0,0,0)为黑色

draw.text((500, 1745), sname, font = ImageFont.truetype(fontpath, 75), fill = (25, 25, 25))
draw.text((585, 2085), cname, font = ImageFont.truetype(fontpath, 50), fill = (25, 25, 25), width=255)
draw.text((1077, 2195), date.year, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
draw.text((1357, 2195), date.month, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
draw.text((1600, 2195), date.day, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
draw.text((1715, 2971), "松江地中海", font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
draw.text((1995, 3100), tname, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
draw.text((1745, 3232), current_time.year, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
draw.text((1961, 3232), current_time.month, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
draw.text((2088, 3232), current_time.day, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))


# 保存图片路径
bk_img.save(r"result.jpg")
# cv2.imwrite("C:\\Users\\25315\\Desktop\\add_text.png", bk_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
print("---------end-----------")
