import os


work_dir = r'C:\Users\zero\Desktop\test'
file_path = os.path.join(work_dir, '梅·25-602.pdf')
result_dir = os.path.join(work_dir, 'result')

class PDFTool():
    def __init__(self):

        from PyPDF2 import PdfFileReader, PdfFileWriter
        self.PdfFileReader = PdfFileReader
        self.PdfFileWriter = PdfFileWriter


    def pdf_split(self, file_path, result_dir, suffix=""):
        with open(file_path, 'rb') as f:
            reader = self.PdfFileReader(f)

            nums = reader.getNumPages()
            for page in range(nums):
                writer = self.PdfFileWriter() 
                writer.addPage(reader.getPage(page))
                out_file = os.path.join(result_dir, "%s%s.pdf" %(str(page+1).zfill(3), suffix))

                print('拆分 第%s页 ' %(page+1))
                with open(out_file, 'wb') as outf:
                    writer.write(outf)

    def pdf_merge(self, file_dir, out_file_path):
        writer = self.PdfFileWriter() 
        files = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir) 
                    if file_name.endswith('pdf')
        ]
        file_objs = [open(file_path, 'rb') for file_path in files
                    if os.path.isfile(file_path)]

        print(file_objs)

        for obj in file_objs:
            reader = self.PdfFileReader(obj)
            nums = reader.getNumPages()
            for page in range(nums):
                print(page)
                writer.addPage(reader.getPage(page))

        with open(out_file_path, 'wb') as outf:
            writer.write(outf)

        for obj in file_objs:
            obj.close()


# pdft = PDFTool()
# pdft.pdf_split(file_path, result_dir)

# out_file_path = r'C:\Users\zero\Desktop\test\result\r\test.pdf'
# pdft.pdf_merge(result_dir, out_file_path)

pdf_path = r'C:\Users\zero\Desktop\test\extract table\SAP-PS模块常用table.pdf'

def extract_table(pdf_path, pages='all', mode=""):
    import pdfplumber


    with pdfplumber.open(pdf_path) as pdf:
        pdf_pages = pdf.pages
        page_count = len(pdf_pages)

        print("共%s 页" %page_count)
        if pages == "all":
            pages = range(page_count)
        else:
            pages = pages

        for page in pages:
        
            for row in pdf_pages[page].extract_tables():
                print(row)
                print(row[0])

extract_table(pdf_path, pages=[0])


import tabula

tables = tabula.read_pdf(pdf_path, pages='all')

# print(len(tables))
# print(tables[3])

# import camelot

# tables = camelot.read_pdf(pdf_path, )
# print(tables)
