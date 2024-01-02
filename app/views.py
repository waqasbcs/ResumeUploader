from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'home.html', {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to the home page after successfully saving the form
            return redirect('home')  # Replace 'home' with your URL name for the home page

class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'candidate.html', {'candidate': candidate})
