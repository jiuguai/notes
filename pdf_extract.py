class PDFTool():

    @staticmethod
    def pdf_split(file_path, result_dir, suffix=""):
        from PyPDF2 import PdfFileReader, PdfFileWriter
        with open(file_path, 'rb') as f:
            reader = PdfFileReader(f)

            nums = reader.getNumPages()
            for page in range(nums):
                writer = PdfFileWriter() 
                writer.addPage(reader.getPage(page))
                out_file = os.path.join(result_dir, "%s%s.pdf" %(str(page+1).zfill(3), suffix))

                print('拆分 第%s页 ' %(page+1))
                with open(out_file, 'wb') as outf:
                    writer.write(outf)


    @staticmethod
    def pdf_merge(file_dir, out_file_path):
        from PyPDF2 import PdfFileReader, PdfFileWriter
        writer = PdfFileWriter() 
        files = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir) 
                    if file_name.endswith('pdf')
        ]
        file_objs = [open(file_path, 'rb') for file_path in files
                    if os.path.isfile(file_path)]

        # print(file_objs)

        for obj in file_objs:
            reader = PdfFileReader(obj)
            nums = reader.getNumPages()
            print(obj)
            for page in range(nums):
                print(page)
                writer.addPage(reader.getPage(page))

        with open(out_file_path, 'wb') as outf:
            writer.write(outf)

        for obj in file_objs:
            obj.close()


    @staticmethod
    def extract_table(pdf_path, pages='all', mode="L"):
        """
        Arguments:
            pdf_path {str} -- path
        
        Keyword Arguments:
            pages {str} --  (default: {'all'})
                  {list} -- [1, 2, 3]
            mode {str} -- L return List
                       -- D return DataFrame List

        """
        mode = mode.upper()
        if mode == "L":
            import pdfplumber

            with pdfplumber.open(pdf_path) as pdf:
                pdf_pages = pdf.pages
                page_count = len(pdf_pages)

                print("共%s 页" %page_count)
                if pages == "all":
                    pages = range(page_count)
                else:
                    pages = [page-1 for page in pages]

                data = []

                for page in pages:
                    for row in pdf_pages[page].extract_tables():
                        data.extend(row)

                return data

        elif mode == "D":
            import tabula
            tables = tabula.read_pdf(pdf_path, pages=pages) 
            print("共%s 页" %len(tables))

            return tables


if __name__ == "__main__":
    pdf = PDFTool()
    file_path = r"C:\Users\Administrator\Desktop\T\pdf\123.pdf"
    result = pdf.extract_table(file_path,mode="D")
    print(result)    