from django.shortcuts import render


# Create your views here.





def test(request):


    a = "Testing"
    context = {
        "a" : a
    }
    template_name = "test.html"
    return render(request, template_name, context)
