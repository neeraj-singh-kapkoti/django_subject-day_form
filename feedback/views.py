
from django.shortcuts import render 
from django.contrib import messages
from feedback.models import Contact
def contact(request):
    if request.method == "POST":
        topic = request.POST.get('topic')
        subject = request.POST.get('subject')
        day = request.POST.get('day')
        contact = Contact(topic=topic,subject=subject,day=day)
        contact.save()
        messages.success(request, 'your message has been send ')
    return render(request,'contact.html')