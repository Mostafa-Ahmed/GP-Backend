from django.views import generic
from django.shortcuts import render, redirect
from .models import Image
from .forms import CreateImage
from django.contrib.auth.mixins import LoginRequiredMixin


def home_page(request):
    return render(request, 'classifier/home_page.html')


class IndexView(LoginRequiredMixin, generic.View):
    template_name = 'classifier/profile.html'

    def get(self, request):
        user = request.user
        images = user.image_set.all()
        return render(request, self.template_name, {'Images': images})


class Upload(LoginRequiredMixin, generic.View):
    model = Image
    fields = CreateImage()
    template_name = 'classifier/image_form.html'
    login_url = '/accounts/login'

    def get(self, request):
        return render(request, self.template_name, {'form': self.fields})

    def post(self, request):
        form = CreateImage(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('classifier:all-images')


class DetailView(LoginRequiredMixin, generic.View):
    template_name = 'classifier/detail.html'

    def get(self, request, pk):
        model = Image.objects.get(id=pk)
        if request.user.id == model.user.id:
            return render(request, self.template_name, {'image': model})
        return redirect('classifier:all-images')