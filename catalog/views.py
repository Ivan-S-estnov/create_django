from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from catalog.forms import CatalogForm
from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse("Данные отправлены.")
    return render(request, "contacts.html")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = CatalogForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = CatalogForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")