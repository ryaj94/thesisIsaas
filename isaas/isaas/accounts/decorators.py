from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
         if request.user.is_authenticated:
             return redirect("home")
         else:
             return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('this page is for students only')
        return wrapper_func
    return decorator


def student_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'forapproval':
            messages.error(request, "Please wait for the approval of the admin! ")
            return render(request, 'accounts/index.html')

        if group == 'admin':
            adviserprof = request.user.adviserprof
            context = {'adviserprof': adviserprof}
            return render(request, 'accounts/AdviserProfile.html', context)

        if group == 'student':
            return view_func(request, *args, **kwargs)

        
            


    return wrapper_function