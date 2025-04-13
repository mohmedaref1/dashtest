from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import User, Department
from .forms import TeamMemberForm

@login_required
def team_dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user)  # Create Task model if needed
    return render(request, 'team/dashboard.html', {'tasks': tasks})

@login_required
def team_management(request):
    members = User.objects.filter(role__in=['admin', 'team'])
    return render(request, 'team/manage.html', {'team_members': members})

@login_required
def shift_start(request):
    if request.method == 'POST':
        request.user.shift_active = True
        request.user.save()
        return render(request, 'partials/shift_indicator.html')
    return redirect('team:manage')

@login_required
def shift_end(request):
    if request.method == 'POST':
        request.user.shift_active = False
        request.user.save()
        return render(request, 'partials/shift_indicator.html')
    return redirect('team:manage')

@login_required
def add_member(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member added successfully')
            return redirect('team:manage')
    else:
        form = TeamMemberForm()
    return render(request, 'team/member_form.html', {'form': form})

@login_required
def edit_member(request, member_id):
    member = get_object_or_404(User, id=member_id)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member updated successfully')
            return redirect('team:manage')
    else:
        form = TeamMemberForm(instance=member)
    return render(request, 'team/member_form.html', {'form': form})

@login_required
def delete_member(request, member_id):
    member = get_object_or_404(User, id=member_id)
    if request.method == 'POST':
        member.delete()
        messages.success(request, 'Member deleted successfully')
    return redirect('team:manage')

def close_popup(request):
    return render(request, 'partials/close_popup.html')