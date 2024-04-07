from django.http import HttpResponse
from django.shortcuts import redirect




from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/admindashboard')
        else:
            response = view_func(request, *args, **kwargs)
            if response is None:
                # If the view function returned None, return a default response
                return HttpResponse("This page requires authentication.")
            else:
                return response

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
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            print(f"User's group: {group}")

        if group == 'donor':
            return redirect('donordashboard')
        elif group == 'ngo':
            return redirect('ngodashboard')
        elif group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            print("User is not in any specified group.")
            print(f"User details: {request.user}")
            return HttpResponse('You are not authorized to view this page')

    return wrapper_function
