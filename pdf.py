import PyPDF2

inputs = ['dummy.pdf', 'tilt.pdf', 'twopage.pdf']


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write('super.pdf')

    add_watermark('super.pdf')


def add_watermark(pdf_file):
    template = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)


pdf_combiner(inputs)
