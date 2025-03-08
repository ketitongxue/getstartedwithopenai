import pdfplumber
import os

# 打开 PDF 文件
class ParsePdf:
    def __init__(self):
        self.pdf_path = os.getenv("FILEPATH", "/Users/keti/Documents/Demo/getstartedwithopenai/files/The_Old_Man_of_the_Sea.pdf")

    def transpdf(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            # 获取 PDF 的元数据
            metadata = pdf.metadata
            # print(f"PDF Metadata: {metadata}")
            # print(type(metadata))
            title = metadata.get("Title")
            print(f"PDF Title:{title}")
            
            # 获取 PDF 的页数
            num_pages = len(pdf.pages)
            print(f"Number of Pages: {num_pages}")
            
            # 遍历所有的页面并存储到 list 中
            # content = []
            with open(title+".txt", 'w') as f :
                for num_page in range(num_pages):
                    page1_text = pdf.pages[num_page].extract_text()
                    # content.append(page1_text)
                    print(f"Page {num_page} Text:\n")
                    print(page1_text)
                    f.write(page1_text)