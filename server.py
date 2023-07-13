from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from PIL import ImageFont, ImageDraw, Image
from io import BytesIO


app = FastAPI()

# 添加跨域支持中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class FormData(BaseModel):
    sname: str
    cname: str
    date: str
    tname: str


@app.post('/api/ending')
def process_form_data(data: FormData = {"sname": "陈思宇", "cname": "周日 14:45", "date": "2023-7-13", "tname": "杨斌"}):
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

    # 保存图片到字节流
    image_bytes = BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    # 保存图片路径
    bk_img.save(r"result.jpg")
    # cv2.imwrite("C:\\Users\\25315\\Desktop\\add_text.png", bk_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    print("---------end-----------")


    return image_bytes