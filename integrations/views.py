from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import APIIntegration
from .forms import APIIntegrationForm

@login_required
def integrations_dashboard(request):
    integrations = APIIntegration.objects.filter(created_by=request.user)
    return render(request, 'integrations/dashboard.html', {
        'integrations': integrations
    })

@login_required
def create_integration(request):
    if request.method == 'POST':
        form = APIIntegrationForm(request.POST)
        if form.is_valid():
            integration = form.save(commit=False)
            integration.created_by = request.user
            integration.save()
            return redirect('integrations:dashboard')
    else:
        form = APIIntegrationForm()
    return render(request, 'integrations/form.html', {'form': form})

@login_required
def test_integration(request, integration_id):
    integration = APIIntegration.objects.get(id=integration_id)
    # Add actual test logic
    return render(request, 'integrations/test_result.html', {
        'integration': integration
    })