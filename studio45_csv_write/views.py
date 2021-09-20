import csv
import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def write_data_from_csv(request):
    NAME = ['Riya', 'Suzzane', 'George', 'Zoya', 'Smith', 'Henry']
    SUBJECT = ['CHE', 'PHY', 'CHE', 'BIO', 'ENG', 'ENG']
    current_date_and_time = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    file_name = 'report_' + current_date_and_time + '.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename='+file_name
    writer = csv.writer(response)
    writer.writerow(['Student Name', 'Quiz Subject'])
    for (name, sub) in zip(NAME, SUBJECT):
        writer.writerow([name, sub])
    return response

def read_data_to_csv(request):
    file_name = 'testing.csv'
    path = 'upload_csv'
    full_path = os.path.join(path, file_name)
    csv_file = open(full_path, 'r', encoding='utf-8')
    reader = csv.reader(csv_file)
    for row in reader:
        print(" ".join(row[0:]))
    return HttpResponse('Data from CSV file read successfully.')
