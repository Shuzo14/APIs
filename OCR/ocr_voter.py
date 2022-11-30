import pytesseract, re
from PIL import Image

def findword(textlist, wordstring):
    lineno = -1
    for wordline in textlist:
        xx = wordline.split( )
        if ([w for w in xx if re.search(wordstring, w)]):
            lineno = textlist.index(wordline)
            textlist = textlist[lineno+1:]
            return textlist
    return textlist

def voterid_read_data(image):

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(image)
    text = pytesseract.image_to_string(img, lang ="eng")
            
    text1 = []
    
    # Splitting the lines to sort the text paragraph wise
    lines = text.split('\n')
    for lin in lines:
        s = lin.strip()
        s = s.rstrip()
        s = s.lstrip()
        text1.append(s)
        
    # Finding the electors number 
    voter_no = findword(text1, '(ELECTION COMMISSION OF INDIA|CARD|IDENTITY CARD)$')
    voter_no = voter_no[0]
    voter_no = voter_no.replace(" ", "")
        
    lines = text
        
    for x in lines.split('\n'):
        _ = x.split()
        if ([w for w in _ if re.search("(Elector's|ELECTOR'S)$", w)]):    
            person_name = x
            person_name = person_name.split(':')[1].strip()
            full_name = person_name
                
        # Finding the father/husband/mother name        
        if ([w for w in _ if re.search("(Father's|Mother's|FATHER'S|MOTHER'S)$", w)]):
            elder_name = x
            elder_name = elder_name.split(':')[1].strip()
                
        # Finding the gender of the electoral candidate
        if ([w for w in _ if re.search('(Male|MALE|male)$', w)]):
            sex = "Male"
        elif ([w for w in _ if re.search('(Female|FEMALE|female)$', w)]):
            sex = "Female"
                
        # Finding the Date of Birth 
        if ([w for w in _ if re.search('(Year|YEAR|Birth|Date|Date of Birth|DATE OF BIRTH|DOB)$', w)]):
            dob = x
            dob = dob.split(':')[1].strip()
    
    # Converting the extracted informaton into json
    data = {
        'Voter Number':voter_no,
        'Elector Name':full_name,
        'Father Name':elder_name,
        'Sex':sex,
        'Date of Birth':dob
    }
    return data

