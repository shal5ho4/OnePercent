from django.shortcuts import render
from .forms import QueryForm

def query_form(request):
  if request.method == 'POST':
    form = QueryForm(request.POST)

    if request.POST.get('next', '') == 'confirm':
      form.save(commit=False) #いる？
      return render(
        request, 'query/form_create.html', {'form': form}
      )
    if request.POST.get('next', '') == 'back':
      form = QueryForm(request.session.get('form_data'))
      return render(
        request, 'query/form.html', {'form': form}
      )
    if request.POST.get('next', '') == 'create':
      form.save(commit=True)
      return render(request, 'query/confirmation.html')
  
  else:
    form = QueryForm()
  return render(request, 'query/form.html')
