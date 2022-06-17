from django.shortcuts import redirect, render
from .models import server, type_of_server,user, application, services,applicaitonshasservices, overall
from .forms import serverForm,type_of_serverForm,usersForm,serviceForm,applicationsForm,overallForm,apphasservicesForm


def getData(request):
    return render(request, 'crud_main/get_data.html')


def create_server(request):
    form = serverForm()
    if request.method == 'POST':
        form = serverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/create_server.html', context)


def itype_of_server(request):
    form = type_of_serverForm()
    if request.method == 'POST':
        form = type_of_serverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/type_of_server.html', context)

    
def iusers(request):
    form = usersForm()
    if request.method == 'POST':
        form = usersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/users.html', context)


def iservices(request):
    form = serviceForm()
    if request.method == 'POST':
        form = serviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/servers.html', context)


def iapphasservices(request):
    form = apphasservicesForm()
    if request.method == 'POST':
        form = apphasservicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/app_has_services.html', context)


def iapplications(request):
    form = applicationsForm()
    if request.method == 'POST':
        form = applicationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/applications.html', context)
    

def ioverall(request):
    form = overallForm()
    if request.method == 'POST':
        form = overallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_main:dataView')
    context = {'form':form}
    return render(request,'crud_main/overall.html', context)



def update_server(request, server_id):
    updateObject = server.objects.get(pk=server_id)
    form = serverForm(request.POST or None, instance=updateObject)
    if form.is_valid():
        form.save()
        return redirect('crud_main:list')
    return render(request, 'crud_main/update_server.html', {'updateObject':updateObject, 'form':form} )


def update_type_of_server(request, type_of_server_id):
    updateObject = type_of_server.objects.get(pk=type_of_server_id)
    form = type_of_serverForm(request.POST or None, instance=updateObject)
    if form.is_valid():
        form.save()
        return redirect('crud_main:list')
    return render(request, 'crud_main/update_type_of_server.html', {'updateObject':updateObject, 'form':form} )


def update_users(request, users_id):
    updateObject = user.objects.get(pk=users_id)
    form = usersForm(request.POST or None, instance=updateObject)
    if form.is_valid():
        form.save()
        return redirect('crud_main:list')
    return render(request, 'crud_main/update_users.html', {'updateObject':updateObject, 'form':form} )

def update_services(request, services_id):
    updateObject = services.objects.get(pk=services_id)
    form = serviceForm(request.POST or None, instance=updateObject)
    if form.is_valid():
        form.save()
        return redirect('crud_main:list')
    return render(request, 'crud_main/update_services.html', {'updateObject':updateObject, 'form':form} )


def update_applications(request, applications_id):
    updateObject = application.objects.get(pk=applications_id)
    form = applicationsForm(request.POST or None, instance=updateObject)
    if form.is_valid():
        form.save()
        return redirect('crud_main:list')
    return render(request, 'crud_main/update_applications.html', {'updateObject':updateObject, 'form':form} )


def updateapphasservices(request, apphasservices_id):
    updateObject = applicaitonshasservices.objects.get(pk=apphasservices_id)
    form = apphasservicesForm(request.POST or None, instance=updateObject)
    if form.is_valid():
        form.save()
        return redirect('crud_main:list')
    return render(request, 'crud_main/updateapphasservices.html', {'updateObject':updateObject, 'form':form} )


def update_overall(request, overall_id):
    updateObject = overall.objects.get(pk=overall_id)
    form = overallForm(request.POST or None, instance=updateObject)
    if form.is_valid():
        form.save()
        return redirect('crud_main:list')
    return render(request, 'crud_main/update_overall.html', {'updateObject':updateObject, 'form':form} )

    

def deleteServer(request,pk):
    serverObject = server.objects.get(server_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_server.html', context)


def deleteTypeofserver(request,pk):
    serverObject = type_of_server.objects.get(type_server_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_type_of_server.html', context)


def deleteUsers(request,pk):
    serverObject = user.objects.get(user_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_users.html', context)


def deleteServices(request,pk):
    serverObject = services.objects.get(service_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_servers.html', context)


def deleteApplications(request,pk):
    serverObject = application.objects.get(app_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_apphasservices.html', context)

def deleteapphasservices(request, pk):
    serverObject = applicaitonshasservices.objects.get(app_id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_applications.html', context)


def deleteOverall(request,pk):
    serverObject = overall.objects.get(id = pk)
    if request.method == 'POST':
        serverObject.delete()
        return redirect('crud_main:dataView')
    context = {'object':serverObject}
    return render(request, 'crud_main/delete_template_overall.html', context)



def list (request):
    serverlist = server.objects.all()
    type_of_serverlist = type_of_server.objects.all()
    userslist = user.objects.all()
    serverslist = services.objects.all()
    applicationslist = application.objects.all()
    applicationhasservices = applicaitonshasservices.objects.all()
    overalllist = overall.objects.all()
    context = {'server':serverlist,'type_of_server':type_of_serverlist,'users':userslist,'servers':serverslist,'applications':applicationslist,'applicationshasservices':applicationhasservices,'overall':overalllist}
    return render(request, 'crud_main/list.html', context)



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        server = server.objects.filter(name__contains=searched)

        return render(request,'crud_main/search.html',{'searched': searched, 'server': server})
    else:
        return render(request, 'crud_main/search.html',{})

def show_server(request, server_id):
    serv = server.objects.get(pk=server_id)
    return render(request, 'crud_main/show_server.html',{'serv': serv})
