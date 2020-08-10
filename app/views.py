from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'

    with open("inflation_russia.csv") as file:
        rows = csv.reader(file, delimiter=";")
        context = {'Statistics': list(rows)}

    return render(request, template_name, context)