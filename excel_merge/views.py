# views.py
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
import io

def upload_files(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')

        # Create an empty DataFrame to store the merged data
        merged_df = pd.DataFrame()

        # Iterate over each uploaded file
        for file in files:
            # Read the uploaded file using pandas
            df = pd.read_excel(file)

            # Select the specified columns
            selected_columns = ['B', 'F', 'G']
            df_selected = df[selected_columns]

            # Append the selected columns to the merged DataFrame
            merged_df = pd.concat([merged_df, df_selected])

        # Generate a new Excel file
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            merged_df.to_excel(writer, index=False, sheet_name='Sheet1')
        output.seek(0)

        # Set the appropriate response headers
        response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        my_text_value = request.POST.get('my_text_field')
        print(my_text_value)
        combined_file_name = my_text_value+".xlsx"
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(combined_file_name)
        return response

    return render(request, 'upload.html')

# views.py
# import pandas as pd
# from django.shortcuts import render
# from django.http import HttpResponse
# import io

# def upload_file(request):
#     if request.method == 'POST':
        # Assuming your form has <input type="file" name="file" />
        # file = request.FILES['file']

        # Read the uploaded file using pandas
        # df = pd.read_excel(file)

        # Select the specified columns
        # selected_columns = ['B', 'F', 'G']
        # df_selected = df[selected_columns]

        # Generate a new Excel file
        # output = io.BytesIO()
        # with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        #     df_selected.to_excel(writer, index=False, sheet_name='Sheet1')
        # output.seek(0)

        # Set the appropriate response headers
    #     response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    #     response['Content-Disposition'] = 'attachment; filename=rearranged_file.xlsx'
    #     return response

    # return render(request, 'upload.html')
