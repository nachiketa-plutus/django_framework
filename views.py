# This has been created by Nachiketa Buddha!
from django.http import HttpResponse

def Home(request):
    return HttpResponse("<h2>This will very shortly display the HOME section of the textutils project <br><br>"
                        "And hello! This is Nachiketa! "
                        '''<br><br> <button onclick="document.location='http://127.0.0.1:8000/About'"> <strong><h2>About<h2></strong> </button></h2>'''
                        '''<hr><button onclick="document.location='http://127.0.0.1:8000/removepunctuation'"> <strong><h2>Remove Punctuation Page<h2></strong> </button>&nbsp&nbsp&nbsp</h2>'''
                        '''<button onclick="document.location='http://127.0.0.1:8000/capitalizefirst'"> <strong><h2>Capitalize First Letter Page<h2></strong> </button>&nbsp&nbsp&nbsp</h2>'''
                        '''<button onclick="document.location='http://127.0.0.1:8000/removespace'"> <strong><h2>Remove Spaces Page<h2></strong> </button></h2>")''')

def About(request):
    return HttpResponse("This is an about page for textutils project by Nachiketa! <br><br> "
                        '''<button onclick="document.location='http://127.0.0.1:8000'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')

def removepunctuation(request):
    return HttpResponse("This is the page for removing punctuations in the textutils project by Nachiketa! <br><br> "
                        '''<button onclick="document.location='http://127.0.0.1:8000'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')

def capitalizefirst(request):
    return HttpResponse("This is the page to capitalize first letter of each word in the textutils project by Nachiketa! <br><br> "
                        '''<button onclick="document.location='http://127.0.0.1:8000'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')

def removespace(request):
    return HttpResponse("This is the page to remove spaces in the textutils project by Nachiketa! <br><br> "
                        '''<button onclick="document.location='http://127.0.0.1:8000'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')





#
#
#
# # def links(request):
# #     return HttpResponse('''<h1>Personal Navigator for some of the top few websites I surf.</h1>
# #                         <a href="https://www.programiz.com/python-programming/file-operation" target="_blank">
# #                         File Operation on Programmiz </a><br><br>
# #                         <a href="https://www.geeksforgeeks.org/open-a-file-in-python/" target="_blank">
# #                         Visit GeeksForGeeks for File Operations in Python. </a>''')
#
# '''To open an existing file on the django server or website'''
# '''
# ----------------------------------------
# Pass the content variable defined above,
# to read the existing file named myFile.txt. Path is passed too.
# -------------------------------------------
# '''
# # def file(request):
# #     f=open("C:/New folder/myFile.txt")
# #     content1=f.read()
# #     return HttpResponse(content1)
# # def file2(request):
# #     with open("C:/New folder/myFile1.txt") as file:
# #         content=file.read()
# #     return HttpResponse(content)
#
#
