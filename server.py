from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Body
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
            # self.month = f"{self.month:0>2}"
            # self.day = f"{self.day:0>2}"

    print("---------start-----------")

    # 获取参数
    sname: str = data['sname']
    cname: str = data['cname']
    date: Date = Date(data['date'])
    tname: str = data['tname']
    bk_img_path = r"结课通知单.jpg"
    current_time: Date = Date(time.strftime("%Y-%m-%d"))
    school: str = data['school']
    
    # 图片路径
    bk_img = Image.open(bk_img_path)

    #设置需要显示的字体
    fontpath = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"     
    draw = ImageDraw.Draw(bk_img)

    # 班级名称规范化
    if "：" in cname:
        cname = cname.replace("：", ":")
    if cname[2]!=' ':
        cname = cname[:2] + ' ' + cname[3:]
    
    draw.text((500, 1729), sname, font = ImageFont.truetype(fontpath, 75), fill = (25, 25, 25))
    draw.text((585, 2085), cname, font = ImageFont.truetype(fontpath, 50), fill = (25, 25, 25), width=255)
    draw.text((1069, 2181), date.year, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
    draw.text((1364, 2181), date.month, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
    draw.text((1607, 2181), date.day, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
    draw.text((1715, 2962), school, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
    draw.text((1973, 3081), tname, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
    draw.text((1727, 3220), current_time.year, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
    draw.text((1955, 3220), current_time.month, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))
    draw.text((2081, 3220), current_time.day, font = ImageFont.truetype(fontpath, 70), fill = (25, 25, 25))

    # 保存图片到字节流
    bk_img.save("temp.jpg", format='JPEG')
    
    print("---------end-----------")

    return {"status": 1}

@app.get("/api/ending/{file}")
def get_file(file: str):
    return FileResponse("temp.jpg", media_type="application/octet-stream")

app.mount("/api/ending", StaticFiles(directory="./web/html/", html=True), name="static")

@app.get("/api/ending")
async def index_response():
    return FileResponse("./web/html/index.html")

@app.options("/api/ending")
def check_options():
    return 1

@app.get("/{type}/{file}")
def page_load(type:str, file:str):
    return FileResponse(f'./web/{type}/{file}')