import os.path
import tempfile
import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from main.models import Employees


# Create your views here.
@csrf_exempt
def parse(request):
    path = os.path.join(tempfile.mkdtemp(), 'import.xlsx')
    with open(path, 'wb+') as f:
        for chunk in request.FILES['file'].chunks():
            f.write(chunk)
    df = pd.read_excel(path)
    df = df.replace(np.nan, None)

    for line in df.to_dict('records'):
        employee = Employees.objects.filter(id_number=line['ИИН'])
        if employee:
            pass
        else:
            Employees.objects.create(full_name=line['Имя'], id_number=line['ИИН'])
    return HttpResponse('OK')
