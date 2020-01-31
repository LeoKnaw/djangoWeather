from django.shortcuts import render

# Create your views here.


def home(request):
    global category_desc, category_color
    import json, requests

    try:
        apiReq = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92203&distance=25&API_KEY=DCCBBEE4-357D-4874-8E3B-E6EB8CC6D3F2')
        api = json.loads(apiReq.content)
    except Exception as e:
        api = None

    if api[0]['AQI'] <= 50:
        category_desc = 'Air quality is considered satisfactory, and air pollution poses little or no risk.'
        category_color = 'good'
    elif api[0]['AQI'] <= 100:
        category_desc = 'Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution'
        category_color = 'moderate'
    elif api[0]['AQI'] <= 150:
        category_desc = 'Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
        category_color = 'usg'
    elif api[0]['AQI'] <= 200:
        category_desc = 'Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
        category_color = 'unhealthy'
    elif api[0]['AQI'] <= 300:
        category_desc = 'Health alert: everyone may experience more serious health effects.'
        category_color = 'very-unhealthy'
    elif api[0]['AQI'] <= 500:
        category_desc = 'Health warnings of emergency conditions. The entire population is more likely to be affected.'
        category_color = 'hazardous'

    context = {
        'api': api,
        'category_desc': category_desc,
        'category_color': category_color
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')