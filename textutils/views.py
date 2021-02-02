'''Short documentation for functions defined.'''
# This has been created by Nachiketa Buddha!
from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'index.html')

    # return HttpResponse("<h2>This will very shortly display the HOME section of the textutils project <br><br>"
    #                     "And hello! This is Nachiketa! "
    #                     '''<br><br> <button onclick="document.location='http://127.0.0.1:8000/About'"> <strong><h2>About<h2></strong> </button></h2>'''
    #                     '''<hr><button onclick="document.location='http://127.0.0.1:8000/removepunctuation'"> <strong><h2>Remove Punctuation Page<h2></strong> </button>&nbsp&nbsp&nbsp</h2>'''
    #                     '''<button onclick="document.location='http://127.0.0.1:8000/capitalizefirst'"> <strong><h2>Capitalize First Letter Page<h2></strong> </button>&nbsp&nbsp&nbsp</h2>'''
    #                     '''<button onclick="document.location='http://127.0.0.1:8000/removespace'"> <strong><h2>Remove Spaces Page<h2></strong> </button></h2>&nbsp&nbsp&nbsp'''
    #                     '''<button onclick="document.location='http://127.0.0.1:8000/newlineremove'"> <strong><h2>Remove New Lines Page<h2></strong> </button></h2>&nbsp&nbsp&nbsp'''
    #                     '''<button onclick="document.location='http://127.0.0.1:8000/newlineremove'"> <strong><h2>Characters Count Page<h2></strong> </button></h2><br><br>''')

def about(request):
    return HttpResponse("<h2>This is an about page for textutils project by Nachiketa!</h2> <br><br> "
                        '''<button onclick="document.location='http://127.0.0.1:8000'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')

def analyze(request):
    #Getting text
    djangoText=print(request.GET.get('text','default'))

    #redirecting to analyze page of the project.
    return render(request, 'analyze.html')

def remove_punctuation(request):
    return HttpResponse("<h2>This is the page for removing punctuations in the textutils project by Nachiketa! </h2> <br><br> "
                        '''<button onclick="document.location='http://127.0.0.1:8000/'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')

def capitalize_first(request):
    return HttpResponse("<h2>This is the page to capitalize first letter of each word in the textutils project by Nachiketa! </h2> <br><br> "
                        '''<button onclick="document.location='http://127.0.0.1:8000'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')

def remove_space(request):
    return HttpResponse("<h2>This is the page to remove spaces in the textutils project by Nachiketa! <br><br> </h2>"
                        '''<button onclick="document.location='http://127.0.0.1:8000/'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')

def newline_remove(request):
    return HttpResponse("<h2>This is the page to remove a newer line in the textutils project by Nachiketa! <br><br> </h2>"
                        '''<button onclick="document.location='http://127.0.0.1:8000'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')

def char_count(request):
    return HttpResponse("<h2>This is the page to count characters wherever required in the textutils project by Nachiketa! <br><br> </h2>"
                        '''<button onclick="document.location='http://127.0.0.1:8000/'"><strong><h2>Back to Main Page<h2></strong></button></h2>''')







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
