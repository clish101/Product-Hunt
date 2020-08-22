from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'products/home.html', context)


class createProductview(LoginRequiredMixin, CreateView):
    model = Product
    context_object_name = 'product'
    fields = ['title', 'url',
              'image', 'icon', 'body']

    def form_valid(self, form):
        form.instance.hunter = self.request.user
        return super().form_valid(form)


class productDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'


def votes(request, vote_pk):
    if request.method == 'POST':
        vote = get_object_or_404(Product, pk=vote_pk)
        vote.votes_total += 1
        vote.save()
        return redirect(vote)
