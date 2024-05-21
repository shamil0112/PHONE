from django.shortcuts import render, redirect
from .models import people



def home(request):
    return render(request, "home.html")

def table(request):
    people_list = people.objects.all()
    return render(request, "table.html",{'people_list': people_list})

def main(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['num']
        place = request.POST['place']
        
        ppl = people(name=name, number=number, place=place)
        ppl.save()
        return redirect('table')  
        
    
        
    return render(request, 'main.html', )

def Delete_contact(request,id):
    a=people.objects.get(id=id)
    a.delete()
    return redirect("table")


def edit_person(request, pk):
    persons = people.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['num']
        place = request.POST['place']
        
        persons.name = name
        persons.number = number
        persons.place = place
        persons.save()
        return redirect('table')
    
    return render(request, 'edit.html', {'person': persons})
        
    