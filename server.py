from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, Body
from pydantic import BaseModel
from PIL import ImageFont, ImageDraw, Image
import time
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


app = FastAPI()

# 添加跨域支持中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


# class FormData(BaseModel):
#     sname: str
#     cname: str
#     date: str
#     tname: str


@app.post('/api/ending')
def process_form_data(data = Body()):
    print(data)
    class Date():
        def __init__(self, date):
            self.year, self.month, self.day = date.split('-')
            self.month = f"{self.month:0>2}"
            self.day = f"{self.day:0>2}"

    print("---------start-----------")

    # 获取参数
    sname: str = data['sname']
    cname: str = data['cname']
    date: Date = Date(data['date'])
    tname: str = data['tname']
    bk_img_path = r"结课通知单.jpg"
    current_time: Date = Date(time.strftime("%Y-%m-%d"))

    # 图片路径
    bk_img = Image.open(bk_img_path)

    #设置需要显示的字体
    fontpath = "font/simsun.ttc"    
    draw = ImageDraw.Draw(bk_img)

    # 班级名称规范化
    if "：" in cname:
        cname = cname.replace("：", ":")
    if cname[2]!=' ':
        cname = cname[:2] + ' ' + cname[3:]
    
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
    bk_img.save("temp.jpg", format='JPEG')
    
    print("---------end-----------")

    return {"status": 1}

@app.get("/{type}/{file}")
def page_load(type:str, file:str):
    return FileResponse(f'./web/{type}/{file}')

@app.get("/api/ending/{file}")
def get_file(file: str):
    return FileResponse("temp.jpg", media_type="application/octet-stream")

app.mount("/api/ending", StaticFiles(directory="./web/html/", html=True), name="static")
# templates = Jinja2Templates(directory=)

@app.get("/api/ending")
async def index_response():
    return FileResponse("./web/html/index.html")