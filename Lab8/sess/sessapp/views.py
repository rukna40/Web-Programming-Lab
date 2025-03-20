from django.shortcuts import render, redirect
from .forms import FirstPage
# Create your views here.
def first_page(request):
    if request.method=='POST':
        form=FirstPage(request.POST)
        if form.is_valid():
            request.session['name']=form.cleaned_data['name']
            request.session['roll']=form.cleaned_data['roll']
            request.session['subject']=form.cleaned_data['subject']
            return redirect('second_page')
    else:
        form=FirstPage()       
    return render(request, 'firstPage.html', {'form':form})

def second_page(request):
    name = request.session.get('name','Not provided')
    roll = request.session.get('roll','Not provided')
    subject = request.session.get('subject','Not provided')
    
    return render(request, 'secondPage.html',{'name':name,'roll':roll,'subject':subject})