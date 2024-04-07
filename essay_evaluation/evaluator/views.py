# from django.shortcuts import render
# from .forms import UploadForm
# from PyPDF2 import PdfReader

# def upload_and_parse(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             essay_text = ""
#             rubric_text = ""

#             # Get uploaded files using get with default values (None)
#             essay_file = request.FILES.get('essay_file', None)
#             rubric_file = request.FILES.get('rubric_file', None)

#             if essay_file:
#                 reader = PdfReader(essay_file)
#                 for page in reader.pages:
#                     essay_text += page.extract_text()

#             if rubric_file:
#                 reader = PdfReader(rubric_file)
#                 for page in reader.pages:
#                     rubric_text += page.extract_text()

#             # Process or store the extracted texts (optional)
#             return render(request, 'success.html', {'essay_text': essay_text, 'rubric_text': rubric_text})
#         else:
#             # Handle form validation errors
#             return render(request, 'upload.html', {'form': form})
#     else:
#         form = UploadForm()
#     return render(request, 'upload.html', {'form': form})

import requests
from django.shortcuts import render
from .forms import UploadForm
from PyPDF2 import PdfReader


def upload_and_parse(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            essay_text = ""
            rubric_text = ""

            # Get uploaded files
            essay_file = request.FILES.get('essay_file', None)
            rubric_file = request.FILES.get('rubric_file', None)

            # Parse files
            if essay_file:
                reader = PdfReader(essay_file)
                for page in reader.pages:
                    essay_text += page.extract_text()
            if rubric_file:
                reader = PdfReader(rubric_file)
                for page in reader.pages:
                    rubric_text += page.extract_text()

            # Bard API integration
            api_url = "https://bard.googleapis.com/v1/documents:annotateText"
            access_token = "AIzaSyAkFzi_evDjC3DCkqkKipNAEgf3blBJ-GQ"  # Replace with your actual access token

            # Prepare request data
            data = {
                "document": {
                    "content": f"**Essay:**\n{essay_text}\n\n**Rubric:**\n{rubric_text}",
                    "type": "PLAIN_TEXT"
                },
                "features": {
                    "extract_summary": True,
                }
            }
            headers = {"Authorization": f"Bearer {access_token}"}

            # Send request to Bard API
            response = requests.post(api_url, json=data, headers=headers)

            # Extract summary (corrected extraction logic)
            if response.status_code == 200:
                document = response.json()["document"]  # Access the entire document
                summary = document["summary"]  # Extract the summary
            else:
                summary = "Error: Failed to get summary from Bard API."
                print(response.text)

            # Feedback Generation (Pass/Fail based on Criteria)
            feedback = generate_pass_fail_feedback(summary, rubric_text)

            return render(request, 'success.html', {
                'essay_text': essay_text,
                'rubric_text': rubric_text,
                'summary': summary,
                'feedback': feedback
            })
        else:
            # Handle form validation errors
            return render(request, 'upload.html', {'form': form})
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})

# Helper function for feedback generation (replace with your implementation)
def generate_pass_fail_feedback(summary, rubric_text):
    # TODO: Implement your logic to analyze summary and rubric,
    # and generate Pass/Fail feedback based on criteria
    pass


