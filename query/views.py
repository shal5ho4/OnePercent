from django.shortcuts import render
from .forms import QueryForm

def query_form(request):
  if request.method == 'POST':
    form = QueryForm(request.POST)

    if request.POST.get('next', '') == 'back':
      if 'input_data' in request.session:
        input_data = request.session['input_data']
        form = QueryForm(input_data)
      return render(request, 'query/form.html', {'form': form})

    elif request.POST.get('next', '') == 'confirm':
      form = QueryForm(request.POST)
      if form.is_valid():
        input_data = {
          'name': form.cleaned_data['name'],
          'email': form.cleaned_data['email'],
          'phone': form.cleaned_data['phone'],
          'text': form.cleaned_data['text']
        }
        request.session['input_data'] = input_data
        return render(request, 'query/form_create.html', {'form': form})

    elif request.POST.get('next', '') == 'create':
      form = QueryForm(request.POST)
      form.save(commit=True)
      request.session.pop('input_data')
      #メール処理
      #通知処理
      return render(request, 'query/confirmation.html')

  else:
    form = QueryForm()
    return render(request, 'query/form.html', {'form': form})