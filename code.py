import PyPDF2
import pandas as pd
object =open('<University Result. pdf>','rb')
reader = PyPDF2.PdfFileReader(object)
reader.numPages
page= reader.getPage(1)
NAMEP=[]
ROLLP=[]
REGP=[]
CGPAP=[]
text=page.extractText()
text=(text.split('NAME :'))[1]
name=(text[2:].split('\n'))[0]
NAMEP.append(name)
text=(text.split('ROLL NO. :'))[1]
roll=(text[2:].split('\n'))[0]
ROLLP.append(roll)
registration_no=((text.split('REGISTRATION NO : '))[1]).split('\n')[1]
REGP.append(registration_no)
text=(text.split('SEMESTER :'))[1]
cgpa=(float)((text.split('\n'))[0])
CGPAP.append(cgpa)
df=pd.DataFrame({'NAME':NAMEP,'REGISTRATION NO ': REGP,'ROLL NO. ': ROLLP,'CGPA ': CGPAP})
