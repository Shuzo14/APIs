import pytesseract, ftfy, json, re
from PIL import Image

def vehicleRC_read_data(image):
    
    # Defining path to tesseract.exe and the image
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
    try:
        img = Image.open(image)

        try:
            DL = []

            # Extract text from image
            text = pytesseract.image_to_string(img, lang ="eng")
            text = ftfy.fix_text(text)
            text = ftfy.fix_encoding(text)

            # Splitting the lines to sort the text paragraph wise
            lines = text.split('\n')
            for lin in lines:
                s = lin.strip()
                s = s.rstrip()
                s = s.lstrip()
                DL.append(s)
            
            for x in lines:
                _ = x.split()
                if ([w for w in _ if re.search("(Driving Licence|DL No|DL|Licence No|REGN)$", w)]):    
                    dl_number = x
                    #print(dl_number)
                    
                if ([w for w in _ if re.search("(Date of Birth|DOB|D.O.B.)$", w)]):    
                    dl_dob = x.split(':')[1].strip()
                    #print(dob)
                
            dl_data = {
            'DL data' : lines,
            'DL Number' : dl_number,
            'DOB' : dl_dob
            }
            
            return dl_data
        
        except:
            a = {'status':'Failed', 'message': 'Invalid Image' }
            return json.dumps(a)
    
    except:
        a = {'status':'Failed', 'message': 'Invalid Image' }
        return json.dumps(a)

