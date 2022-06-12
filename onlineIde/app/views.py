import sys
import os
import filecmp

from django.shortcuts import render , redirect
from .forms import CodeForm , CustomerRegistrationForm , LoginForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from .models import problem , UserProfile ,ListOfProblem
from django.http import HttpResponseRedirect



cwd = os.getcwd()  
def compre():  
    
    # filehandle1=open('app/file.txt',"r")
    # filehandle2=open('app/t2.txt',"r")
    filehandle1='app/file.txt'
    filehandle2='app/t2.txt'
    # for line1 in filehandle1:
    #     for line2 in filehandle2:
    #         if line1==line2:
    #             return True
    #         else:
    #             return False
    
    
    # shallow comparison
    result = filecmp.cmp(filehandle1, filehandle2)
    return result
def home(request):
    fm = problem.objects.all()
     
    return render(request,'allproblem.html',{'fm':fm})

def allproblem(request,id):
    if request.user.is_authenticated:
        probleDetails = problem.objects.get(id=id)
        print(probleDetails)
        output =""
        codeFlag = "" 
        initdata = ""
        with open("media/"+str(probleDetails.sudoCode),'r') as f:
            line = f.read()
            initdata = initdata+line
        with open('app/defautl.txt','r') as f:
                pass
        
        # fm = CodeForm(initial=initdata)
        fm = CodeForm(initial={"code":initdata})
        if 'run' in request.POST:
            print("=======================================")
            
            if request.method == 'POST':
                print("=============")
                fm = CodeForm(request.POST) 
                if fm.is_valid():
                    codeareadata = fm.cleaned_data['code']
                    

                    try:
                        aea = request.POST.get('my_textarea')   
                        
                        original_stdout = sys.stdout
                        if aea:
                            # if user send input than check here 
                            with open('app/cus.txt', 'w') as f:
                                f.write(aea)   
                            # adding here in codefile
                            with open('app/cus.txt', 'r') as f:
                                codeareadata = codeareadata+"\n"+"x = "+f.read()+"\n"
                                print(codeareadata)
                            
                        else:
                            # here i have reading the input from database for 1
                            with open("media/"+str(probleDetails.input1),'r') as f:
                                codeareadata = codeareadata +"\n"+f.read()+"\n" 
                            print(codeareadata)
                        sys.stdout = open('app/file.txt', 'w')
    
                        with open("media/"+str(probleDetails.funCall)) as f:
                                codeareadata = codeareadata+f.read() 
        
                        exec(codeareadata) 
                        sys.stdout.close()
                        sys.stdout = original_stdout 
                        output = open('app/file.txt', 'r').read()
                        ans = compre()
                        if ans:
                            codeFlag = 'True' 
                        else:
                            codeFlag = 'False'
                        print("-------------------")
                        print(ans)
                        
                        print(aea)
                    except Exception as e:
                        sys.stdout = original_stdout
                        output = e
                        print(e)
        else:
            pass
        return render(request, 'codeing.html',{'fm':fm,'output':output,'flag':codeFlag })
    else:
        return HttpResponseRedirect('/login')

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')

def profileview(request):
    data = UserProfile.objects.get(user=request.user)
    probleList = ListOfProblem.objects.filter(user=request.user)
    count = ListOfProblem.objects.filter(user=request.user).count()
    print(count)
    return render(request, 'profile.html',{'user':data,'listof':probleList , 'count':count})

class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, './customerregistration.html', {'form':form})
  
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! Registered Successfully.')
   form.save()
  return render(request, './customerregistration.html', {'form':form})