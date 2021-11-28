import PyPDF2
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject


def set_need_appearances_writer(writer: PyPDF2.PdfFileWriter) -> PyPDF2.PdfFileWriter:
    try:
        catalog = writer._root_object
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                    NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
                    })

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer
