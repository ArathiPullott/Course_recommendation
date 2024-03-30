from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pandas as pd

def preprocess_data(df):
    # Convert 'published_timestamp' column to datetime
    df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
    return df

def search_courses_by_subject(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        df = pd.read_csv('udemy_courses.csv')
        df = preprocess_data(df)
        filtered_df = df[df['subject'] == subject]
        results = filtered_df[['course_title', 'url', 'price']].values.tolist()
        return render(request, 'search_results.html', {'results': results})
    else:
        return render(request, 'search_form.html')