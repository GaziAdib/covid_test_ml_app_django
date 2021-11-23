from django.shortcuts import render
import pandas as pd
import pickle as pkl
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')



def predict(request):
    model = pd.read_pickle('covid_model.pickle')

    lis = []

    lis.append(request.GET['sex'])
    lis.append(request.GET['intubed'])
    lis.append(request.GET['pneumonia'])
    lis.append(request.GET['age'])
    lis.append(request.GET['diabetes'])
    lis.append(request.GET['copd'])
    lis.append(request.GET['asthma'])
    lis.append(request.GET['hypertension'])
    lis.append(request.GET['cardiovascular'])
    lis.append(request.GET['obesity'])
    lis.append(request.GET['renal_chronic'])
    lis.append(request.GET['tobacco'])
    lis.append(request.GET['contact_other_covid'])
    lis.append(request.GET['icu'])

    print(lis)

    classification = model.predict([lis])

    return render(request, 'predict.html', {'classification': classification[0]})

       

        # result = model.predict([[sex, intubed, pneumonia, age, diabetes, copd, asthma, hypertension, cardiovascular, obesity, renal_chronic, tobacco, contact_other_covid, icu]])

        # classification = result[0]
        # print(classification)

        

        # return JsonResponse({'classification': classification, 'sex': sex, 'intubed': intubed, 'pneumonia': pneumonia, 'age': age, 'diabetes': diabetes, 'copd': copd, 'asthma': asthma, 'hypertension': hypertension, 'cardiovascular': cardiovascular,
        #  'obesity': obesity, 'renal_chronic': renal_chronic, 'tobacco': tobacco, 'contact_other_covid': contact_other_covid, 'icu':icu})

        #return render(request, 'predict.html', {'classification':  classification})
        

       # return JsonResponse({ 'result': classification })



# def predict(request):
#     lis = []
#     if request.POST.get('action') == 'get':
#         sex = int(request.POST.get('sex'))
#         intubed = int(request.POST.get('intubed'))
#         pneumonia = int(request.POST.get('pneumonia'))
#         age = int(request.POST.get('age'))
#         diabetes = int(request.POST.get('diabetes'))
#         copd = int(request.POST.get('copd'))
#         asthma = int(request.POST.get('asthma'))
#         hypertension = int(request.POST.get('hypertension'))
#         cardiovascular = int(request.POST.get('cardiovascular'))
#         obesity = int(request.POST.get('obesity'))
#         renal_chronic = int(request.POST.get('renal_chronic'))
#         tobacco = int(request.POST.get('tobacco'))
#         contact_other_covid = int(request.POST.get('contact_other_covid'))
#         icu = int(request.POST.get('icu'))

    

#         model = pd.read_pickle('covid_model.pickle')

#         result = model.predict([[sex, intubed, pneumonia, age, diabetes, copd, asthma, hypertension, cardiovascular, obesity, renal_chronic, tobacco, contact_other_covid, icu]])

#         classification = result[0]
#         print(classification)

#         return render(request, 'predict.html', {'classification': classification})
