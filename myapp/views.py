from django.shortcuts import render
# from django.shortcuts import render
import os
from django.http import JsonResponse
import pandas as pd
# from functions import create_text_file 
from functions.create_text_file import create_text_file
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
# Create your views here.
def app(request):
    
    return render(request, 'app.html')


def handle_form_submission(request):
    if request.method == 'POST':
        # Process the form data here
        uploaded_file = request.FILES.get('uploaded_file')
        number_of_linksets = int(request.POST.get('number_of_linksets'))
        dpc = request.POST.get('dpc')

        # Perform necessary actions with the form data
        df = pd.read_excel(uploaded_file)

        # Create a list to store rows as dictionaries
        all_rows = []

        # Iterate through rows using iterrows()
        for index, row in df.head(number_of_linksets).iterrows():
            row_dict = row.to_dict()
            all_rows.append(row_dict)

        new_df = pd.DataFrame.from_dict(all_rows)

        # Select column names from the second last row
        column_names = df.iloc[-2]

        # Select the last row for data
        data_row = df.iloc[-1]

        # Create a new DataFrame with extracted column names and data
        params_df = pd.DataFrame([data_row.values], columns=column_names)

        # Generate text content using the create_text_file function
        txt_content = create_text_file(new_df, number_of_linksets, dpc, params_df)

        # Write the content to a temporary file
        temp_file_path = "temp_file.txt"
        with open(temp_file_path, "w") as file:
            file.write(txt_content)

        # Create a response with the file as an attachment
        response = HttpResponse(open(temp_file_path, 'rb').read())
        response['Content-Disposition'] = 'attachment; filename="created_file.txt"'
        response['Content-Type'] = 'text/plain'

        # Clean up temporary file
        os.remove(temp_file_path)

        return response

           



