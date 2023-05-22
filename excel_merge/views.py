import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse

def combine_excel(request):
 if request.method == 'POST':
     files = request.FILES.getlist('files')
     print(files)
     sainathArray = []
     for file in files:
        df = pd.read_excel(file)
        sainathArray.append(df)
     combined = pd.concat(sainathArray)
     combined_file_name = 'combined_file.xlsx'
     combined.to_excel(combined_file_name, index=False)
     with open(combined_file_name, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{combined_file_name}"'

     return response
 return render(request, 'combine_excel.html')

#      return render(request, 'combine_excel.html', {'message': 'Files combined successfully!'})
#  else:
#      return render(request, 'combine_excel.html')



    #  if request.method == 'POST':
    #     files = request.FILES.getlist('files')

    #     combined = pd.DataFrame()
    #     for file in files:
    #         df = pd.read_excel(file)
    #         combined = combined.append(df, ignore_index=True)

    #     combined.to_excel('combined_file.xlsx', index=False)

    #     return render(request, 'combine_excel.html', {'message': 'Files combined successfully!'})
    #  else:
    #     return render(request, 'combine_excel.html')

    # if request.method == 'POST':
    #     files = request.FILES.getlist('files')

    #     combined_data = pd.DataFrame()
    #     for file in files:
    #         df = pd.read_excel(file)
    #         combined_data = combined_data.concat(df)

    #     combined_file_name = 'combined_file.xlsx'
    #     combined_data.to_excel(combined_file_name, index=False)

    #     # Prepare the file for download
    #     with open(combined_file_name, 'rb') as file:
    #         response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    #         response['Content-Disposition'] = f'attachment; filename={combined_file_name}'

    #     return response

    # return render(request, 'combine_excel.html')
