from django.shortcuts import render
from django.contrib import messages
from .forms import QueryForm
from .tasks import query_received, line_notify

def query_form(request):

  if request.method == 'POST':
    form = QueryForm(request.POST)

    # return to edit
    if request.POST.get('next', '') == 'back':

      # retrieve input data from session
      if 'input_data' in request.session:
        input_data = request.session['input_data']
        form = QueryForm(input_data)
      return render(request, 'query/form.html', {'form': form})

    # proceed to confirm
    elif request.POST.get('next', '') == 'confirm':

      # validation
      if form.is_valid():
        input_data = {
          'name': form.cleaned_data['name'],
          'email': form.cleaned_data['email'],
          'phone': form.cleaned_data['phone'],
          'text': form.cleaned_data['text']
        }
        request.session['input_data'] = input_data
        return render(request, 'query/form_create.html', {'form': form})

      # handle invalid data
      else:
        messages.error(request, '※メールアドレスの形式で入力してください。')
        if 'input_data' in request.session:
          input_data = request.session['input_data']
          form = QueryForm(input_data)
        return render(request, 'query/form.html', {'form': form})

    # confirmed then submit the form
    elif request.POST.get('next', '') == 'create':
      form = QueryForm(request.POST)
      query = form.save(commit=True)
      request.session.pop('input_data')
      
      # email notification
      query_received.delay(query.id)
      # LINE notification
      line_notify.delay(query.id)

      return render(request, 'query/confirmation.html')

  else:
    form = QueryForm()
    return render(request, 'query/form.html', {'form': form})