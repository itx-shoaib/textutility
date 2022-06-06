# I have created this file - Shoaib Jamil
from django.http import HttpResponse
from django.shortcuts import render

# video 6
# def programmiz(request):
#     return HttpResponse('''<h1>Navigator</h1> <a href="https://www.programiz.com/python-programming">Programmiz</a>''')
# def w3school(request):
#     return HttpResponse('''<a href="https://www.w3schools.com/python">W3school</a>''')
#
# def codewithharry(request):
#     return HttpResponse('''<a href="https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-16/">Code With Harry</a>''')

# Video 7-Laying the pipeline
def index(request):
    # paramas = {'name' : 'Shoaib' , 'fathername' : 'Jamil','place':'Lahore'}
    return render(request,'index_bs.html')
    # return HttpResponse('''Home''')

def analyze(request):
    # Get the value from chexkboxes
    djtext= request.POST.get('text','default')
    removepunc = request.POST.get('removefcn','off')
    fullcaps = request.POST.get('fullcaps','off')
    removenewline = request.POST.get('removenewline','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    # If and else if for different checkboxes
    if removepunc == "on":
        # analyze = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        paramas = {'purpose':'Removed Puncutations' ,'analyzed_text':analyzed}
        # print(paramas)
        djtext = analyzed
        # analyze the text
        # return HttpResponse('''Remove Punc<br><button><a href="/">back</a></button>''')
        # return render(request,'analyzer_bs.html',paramas)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        paramas = {'purpose': 'Capitalization', 'analyzed_text': analyzed}
        # print(paramas)
        djtext = analyzed
        # return render(request,'analyzer_bs.html',paramas)

    if removenewline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n"and char != "\r":
                analyzed = analyzed + char
            else:
                print("Error")
        paramas = {'purpose': 'Lines Remover', 'analyzed_text': analyzed}
        # print(paramas)
        djtext = analyzed
        # return render(request,'analyzer_bs.html',paramas)

    if extraspaceremover == "on" :
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        paramas = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        # print(paramas)
        djtext = analyzed
        # return render(request,'analyzer_bs.html',paramas)

    if charcount == "on" :
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char
            length = len(analyzed)
            paramas = {'purpose': 'Character count', 'length': length}
        # print(paramas)
        djtext = analyzed
        # return render(request,'charcount_bs.html',paramas)
        # return render(request,'charcount_bs.html',paramas)

    if (removepunc != "on" and fullcaps != "on" and removenewline != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request,'analyzer_bs.html',paramas)