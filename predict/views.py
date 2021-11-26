from django.shortcuts import redirect, render
import pandas as pd
from .models import CovidPrediction
# Create your views here.

def home(request):
    return render(request, 'home.html')



def predict(request):
    model = pd.read_pickle('covid_model.pickle')

    sex = request.GET['sex']
    intubed = request.GET['intubed']
    pneumonia = request.GET['pneumonia']
    age = request.GET['age']
    diabetes = request.GET['diabetes']
    copd = request.GET['copd']
    asthma = request.GET['asthma']
    hypertension = request.GET['hypertension']
    cardiovascular = request.GET['cardiovascular']
    obesity = request.GET['obesity']
    renal_chronic = request.GET['renal_chronic']
    tobacco = request.GET['tobacco']
    contact_other_covid = request.GET['contact_other_covid']
    icu = request.GET['icu']




    lis = []

    lis.append(sex)
    lis.append(intubed)
    lis.append(pneumonia)
    lis.append(age)
    lis.append(diabetes)
    lis.append(copd)
    lis.append(asthma)
    lis.append(hypertension)
    lis.append(cardiovascular)
    lis.append(obesity)
    lis.append(renal_chronic)
    lis.append(tobacco)
    lis.append(contact_other_covid)
    lis.append(icu)

    print(lis)

    classification = model.predict([lis])

    CovidPrediction.objects.create(
        sex=sex,
        intubed=intubed,
        pneumonia=pneumonia,
        age=age,
        diabetes=diabetes,
        copd=copd,
        asthma=asthma,
        hypertension=hypertension,
        cardiovascular=cardiovascular,
        obesity=obesity,
        renal_chronic=renal_chronic,
        tobacco=tobacco,
        contact_other_covid=contact_other_covid,
        icu=icu,
        classification=classification[0]
    )

    return render(request, 'predict.html', {'classification_result': classification[0]})



def db_record(request):
    covid_predictions = CovidPrediction.objects.all()

    context = {
        'covid_records': covid_predictions
    }

    return render(request, 'database.html', context)

       


def delete(request, pk):
    covid_data = CovidPrediction.objects.get(id=pk)
    covid_data.delete()
    return redirect('records')

    

