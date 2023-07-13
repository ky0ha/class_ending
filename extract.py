import PyPDF2 as pdf

pdf_file = open("结课通知单.pdf", 'rb')
pdf_reader = pdf.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)

# 遍历每一页
for page_num in range(num_pages):
    # 获取当前页对象
    page_obj = pdf_reader.pages[page_num]
    # 获取当前页中的所有对象
    page_objs = page_obj['/Resources']['/XObject'].get_object()
    # 遍历每个对象
    for obj_name in page_objs:
        # 判断对象是否为图片
        if page_objs[obj_name]['/Subtype'] == '/Image':
            # 获取图片对象
            img_obj = page_objs[obj_name]
            # 获取图片数据
            img_data = img_obj.get_data()
            # 将图片数据保存为文件
            with open("extract_result.png", '+wb') as f:
                f.write(img_data)
