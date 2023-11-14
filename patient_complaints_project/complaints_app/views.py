from django.shortcuts import render

def patient_complaints(request):
    return render(request, 'complaints_form.html')
