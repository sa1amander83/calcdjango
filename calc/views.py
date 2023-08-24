from django.shortcuts import render


from django.views.generic import FormView
from calc.forms import CalcForm


class CalcView(FormView):
    form_class = CalcForm
    template_name = 'index.html'


    def form_valid(self, form):

        num1 = float(form.cleaned_data['first_number'])
        num2 = float(form.cleaned_data['second_number'])

        if self.request.POST.get('plus'):
            answer = num1 + num2
            sign = '+'
        elif self.request.POST.get('minus'):
            answer = num1 - num2
            sign = '-'
        elif self.request.POST.get('multiply'):
            answer = num1 * num2
            sign = '*'
        else:
            answer = num1 / num2
            sign = '/'
        #вариант 1 отображение на этой же странице
        #return render(self.request, 'index.html', {'answer': answer, 'form': form})


        # вариант 2 как по заданию, переход на другую страницу
        return render(self.request, 'answer.html', {'answer': answer,
                                                    'form': form,'num1':num1, 'num2':num2, 'sign':sign })
