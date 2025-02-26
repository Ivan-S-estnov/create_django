from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.models import Product, NewModel


class NewModelCreateView(CreateView):
    model = NewModel
    fields = ["name", "description"]
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
    fields = ["name", "description"]
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


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
