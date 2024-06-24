from django.shortcuts import render

def calculator(request):
    result = ""
    try:
        if request.method == 'POST':
            num1 = eval(request.POST.get('num1'))
            num2 = eval(request.POST.get('num2'))
            operator = request.POST.get('operator')
            if operator == '+':
                result = int(num1) + int(num2)
            elif operator == '-':
                result = int(num1) - int(num2)
            elif operator == '*':
                result = int(num1) * int(num2)
            elif operator == '/':
                result = int(num1) / int(num2)
            else:
                result = 0
            pass
    except:
        result = "Invalid operator"
    print(result)
    return render(request, 'calculator.html', {'result': result})