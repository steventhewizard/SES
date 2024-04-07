from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RubricForm, EssayForm

def upload_rubric(request):
    if request.method == 'POST':
        form = RubricForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Redirect to a success page
    else:
        form = RubricForm()
    return render(request, 'upload_rubric.html', {'form': form})

def upload_essay(request):
    if request.method == 'POST':
        form = EssayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Redirect to a success page
    else:
        form = EssayForm()
    return render(request, 'upload_essay.html', {'form': form})

