from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.models import Product, NewModel


class NewModelCreateView(CreateView):
    model = NewModel
    fields = ["name", "description", "photo"]
    template_name = "catalog/newmodel_form.html"
    success_url = reverse_lazy("catalog:newmodel_list")


class NewModelListView(ListView):
    model = NewModel
    template_name = "catalog/newmodel_list.html"
    context_object_name = "newmodels"


class NewModelDetailView(DetailView):
    model = NewModel
    template_name = "catalog/newmodel_detail.html"
    context_object_name = "newmodel"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class NewModelUpdateView(UpdateView):
    model = NewModel
    fields = ["name", "description", "photo"]
    template_name = "catalog/newmodel_form.html"
    success_url = reverse_lazy("catalog:newmodel_list")

    def get_success_url(self):
        return reverse("catalog:newmodel_detail", args=[self.kwargs.get("pk")])


class NewModelDeleteView(DeleteView):
    model = NewModel
    template_name = "catalog/newmodel_confirm_delete.html"
    success_url = reverse_lazy("catalog:newmodel_list")


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse("Данные отправлены.")
    return render(request, "contacts.html")


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "price"]
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

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "price"]
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")