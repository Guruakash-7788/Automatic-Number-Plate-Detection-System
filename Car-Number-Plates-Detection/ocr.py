import easyocr

def ocr(path):
    reader = easyocr.Reader(['en'])
    output = reader.readtext(path)
    text = output
    return output

