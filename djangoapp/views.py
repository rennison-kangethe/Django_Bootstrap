from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def property_agent(request):
    return render(request, 'property-agent.html')
def property_list(request):
    return render(request, 'property-list.html')
def property_type(request):
    return render(request, 'property-type.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def my_404(request):
    return render(request, '404.html')
def base(request):
    return render(request, 'base.html')
