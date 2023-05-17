# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from django.urls import reverse
from .forms import MerchantUploadForm
from .models import Merchant
import openpyxl
import os
from pymongo import MongoClient
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def upload_merchants(request):
    if request.method == 'POST':
        form = MerchantUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # save the uploaded file to a directory
            file = form.cleaned_data['file']
            file_path = os.path.join('apps', 'home', 'data', file.name)
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            # process the XLSX file
            workbook = openpyxl.load_workbook(file_path)
            worksheet = workbook.active
            merchants = []
            for row in worksheet.iter_rows(min_row=2):
                merchant_id=row[0].value
                merchant_name = row[1].value
                NameOfAccount_Manager = row[2].value
                VPC_value = row[3].value
                UIGmigs = row[4].value
                Billing = row[5].value
                CF_value = row[6].value
                Salfny = row[7].value
                Lending = row[8].value
                TrxLastMonth  = row[9].value
                TrxCurrentMonth  = row[10].value
                VolumeLastMonth  = row[11].value
                VolumeCurrentMonth  = row[12].value
                ChurnType  = row[13].value
                ChurnVolume  = row[14].value
                ActiveTarget  = row[15].value
                Current_MonthTarget   = row[16].value
                Pre_MonthTarget   = row[17].value
                # create a new Merchant object and save to database
                merchant = Merchant(
                    merchant_id=merchant_id,
                    merchant_name=merchant_name,
                    NameOfAccount_Manager=NameOfAccount_Manager,
                    VPC_value=VPC_value,
                    UIGmigs=UIGmigs,
                    Billing=Billing,
                    CF_value=CF_value,
                    Salfny=Salfny,
                    Lending=Lending,
                    TrxLastMonth=TrxLastMonth,
                    TrxCurrentMonth=TrxCurrentMonth,
                    VolumeLastMonth=VolumeLastMonth,
                    VolumeCurrentMonth=VolumeCurrentMonth,
                    ChurnType=ChurnType,
                    ChurnVolume=ChurnVolume,
                    ActiveTarget=ActiveTarget,
                    Current_MonthTarget=Current_MonthTarget,
                    Pre_MonthTarget=Pre_MonthTarget,
                )
                merchants.append(merchant)

            # connect to MongoDB and insert the documents
            client = MongoClient('localhost:27017', 27017)
            db = client['paymob']
            collection = db['merchants']
            result = collection.insert_many([merchant.to_mongo() for merchant in merchants])

            # redirect to success page
            return redirect('upload_success')
    else:
        form = MerchantUploadForm()
    return render(request, 'ui-tables.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')