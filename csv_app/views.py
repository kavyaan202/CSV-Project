from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import CSVFile
from .tasks import process_csv
from django.http import JsonResponse
import pandas as pd

def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            process_csv.delay(csv_file.file.path)  # Trigger Celery task
            return redirect('file_list')
    else:
        form = CSVUploadForm()
    return render(request, 'csv_app/upload.html', {'form': form})

def search_csv(request):
    query = request.GET.get('query', '')
    data = pd.read_csv("media/uploads/sample.csv")

    if query:
        data = data[data['Product Name'].str.contains(query, case=False, na=False)]

    return JsonResponse(data.to_dict(orient="records"), safe=False)