from django.shortcuts import render

# Create your views here.
def words_view(request):
   return render(request,'testapp/words.html')

def wordcount_view(request):
   mess=request.GET['message']
   words=mess.split()
   return render(request,'testapp/wordcount.html',{'mess':mess,'wl':len(words)})

