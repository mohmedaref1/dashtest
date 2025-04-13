from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout  # Add this import at the top
from django.shortcuts import redirect

@login_required
def dashboard(request):
    if request.user.is_admin:
        template = 'admin/dashboard.html'
    else:
        template = 'team/dashboard.html'
    return render(request, template)

def custom_logout(request):
    logout(request)  # Now properly referenced
    return redirect('login')