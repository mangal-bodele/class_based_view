from django.shortcuts import render,redirect
from django.views import View
from .forms import EmployeeForm
from .models import Employee

class Add_View(View):
    form = EmployeeForm
    template_name = 'crud_app/add.html'
    def get(self, request):
        form = self.form()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args,**kwargs):
       form = self.form(request.POST)
       if form.is_valid():
           form.save()
           return redirect('show_url')
       context = {'form':form }
       return render(request,self.template_name,context)


class Show_View(View):
    form = EmployeeForm
    template_name = 'crud_app/show.html'
    def get(self, request):
        employees = Employee.objects.all()
        context = {'employees': employees}
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('show_url')
    #     context = {'form':form}
    #     return render(request, self.template_name,context)

class Update_View(View):
    form = EmployeeForm
    template_name = 'crud_app/show.html'

    def get(self, request,pk):
        obj = Employee.objects.get(id=pk)
        form = self.form(instance=obj)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = Employee.objects.get(id=pk)
        form = self.form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        context = {'form': form}
        return render(request, self.template_name, context)


class Delete_View(View):
    template_name = 'crud_app/confirm.html'
    form = EmployeeForm
    def get(self, request,pk):
        obj = Employee.objects.get(id=pk)
        form = self.form(instance=obj)
        context = {'form':form}
        return render(request, self.template_name,context)

    def post(self, request,pk):
        obj = Employee.objects.get(id=pk)
        obj.delete()
        return redirect('show_url')

