from django.shortcuts import render,redirect
from django.http import JsonResponse , HttpResponse
from .forms import CoachForm , PlayersForm
from .models import CoachModel,PlayersModel,LoginModel,RegisterModel
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

def Home(request):
    return render(request , 'Home.html')

@csrf_exempt
def Register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if RegisterModel.objects.filter(email=email).exists():
            context = {'message':'User is Already Registred'}
            return render(request , 'register.html',context)
        
        new_user = RegisterModel(name=name,email=email)
        new_user.set_password(password)
        new_user.save()

        new_login = LoginModel(email=email)
        new_login.password = new_user.password
        new_login.save()    

        return render(request,'login.html')
    
    error = {'failed':'Registration Failed'}
    return render(request , 'register.html',error)


@csrf_exempt
def Login(request):
    # print('post request recieved')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            login_user = LoginModel.objects.get(email=email)
        except LoginModel.DoesNotExist:
            return render(request,'login.html',{'Duplicate':'User Do Not Exists'})
        
        if not login_user.check_password(password):
            return render(request,'login.html',{'message': 'Incorrect password'})

            
        request.session['user_email'] = email

        # user_email = request.session.get('user_email')

        # if user_email:
        #     print(f"Logged in user: {user_email}")
        # else:
        #     print("No user is logged in")
        mail = request.POST.get('email')
        context = {'mail': mail}
        return render(request,'admin.html' , context)
    
    return render(request,'login.html',{'message':'Login Failed'}) 


@csrf_exempt
def Logout(request):
    if 'user_email' in request.session:
        del request.session['user_email']

    return render(request,'Home.html',{'message':'LogOut successfull'})

@csrf_exempt
def GetCoachView(request):
    if request.method == 'GET':
        coaches = CoachModel.objects.all()
        # print('this is query set',coaches)
        # coaches_data = list(coaches.values())
        return render(request,'GetCoach.html',{"coaches":coaches })
    
@csrf_exempt
def GetPlayersView(request):
    if request.method == 'GET':
        players =  PlayersModel.objects.select_related('coached_by').all()
        # players_data = list(players)
        return render(request,'GetPlayers.html',{"players":players})
            
@csrf_exempt
def PostFormPlayersView(request):
    form = PlayersForm()
    context = {'form':form}
    return render(request,'PostFormPlayers.html',context)

@csrf_exempt       
def PostCoachFormView(request):
    if request.method == 'GET':
        form = CoachForm()
        context = {'form':form}
    return render(request,'PostCoachForm.html',context)

@csrf_exempt
def PostCoachView(request):
    print('entering to add')
    if request.method == 'POST':
        print('i am inside')
        form = CoachForm(request.POST , request.FILES)
        print('form format',form)
        if form.is_valid():
            print(form.data)
            form.save()
            return render(request,'admin.html',{'message':'Coach Added Sucessfully'},status=201)
        else:
            return render(request,'PostCoachForm.html',{'errors': form.errors}, status=400)

    return render(request,'PostCoachForm.html',{'failed':'failed to add'},status = 405)
        
@csrf_exempt
def PostPlayersView(request):
    if request.method == "POST":
        form = PlayersForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return render(request , 'admin.html',{'message':'Saved succesfully'},status=201)    

    return render(request,'PostFormPlayers.html',{'failed':form.errors},status=405)


def get_coach_or_404(coach_id):
    try:
        return CoachModel.objects.get(id=coach_id)
    except CoachModel.DoesNotExist:
        raise Http404("Coach does not exist")
    
@csrf_exempt
def edit_coach(request, coach_id):
    coach = get_coach_or_404(coach_id)

    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('getCoaches')  # assuming this is the name of the view for listing coaches
    else:
        form = CoachForm(instance=coach)

    return render(request, 'edit_coach.html', {'form': form})


@csrf_exempt
def delete_coach(request, coach_id):
    coach = get_coach_or_404(coach_id)
    
    if request.method == 'POST':
        coach.delete()
        return redirect('getCoaches')  # assuming this is the name of the view for listing coaches
    
    return render(request, 'delete_coach.html', {'coach': coach})
    