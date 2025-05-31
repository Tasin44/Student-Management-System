from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse
from .models import Notification

def index(request):
    return render(request,"Home/index.html")

# def create_notification(user, message):
#     Notification.objects.create(user=user, message=message)

def dashboard(request):#if the notification still not read by the user
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()#it'll store the total num of count of the notification if the user didn't read yet
    return render(request, "students/student-dashboard.html")



def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        notification = Notification.objects.filter(user=request.user)
        notification.delete()#cleared all the file when it should be press on the clear button
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden
