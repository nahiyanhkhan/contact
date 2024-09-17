from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AddContactForm, SearchForm
from .models import Contact


# Create your views here.
def contact_list(request):
    contact_list = Contact.objects.all()

    context = {
        "contacts": contact_list,
    }

    return render(request, "contact_list.html", context=context)


def add_contact(request):

    if request.method == "POST":
        add_contact_form = AddContactForm(request.POST)
        if add_contact_form.is_valid():
            add_contact_form.save()
            return redirect("contact_list")
        else:
            return HttpResponse("Invalid form data")

    add_contact_form = AddContactForm()

    context = {"add_contact_form": add_contact_form}

    return render(request, "add_contact.html", context=context)


def contact_details(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
        return render(request, "contact_details.html", {"contact": contact})
    except Contact.DoesNotExist:
        return HttpResponse("contact does not exist!!!")


def update_contact(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)

        if request.method == "POST":
            contact_form = AddContactForm(request.POST, instance=contact)
            if contact_form.is_valid():
                contact_form.save()
                return redirect("contact_list")
            else:
                return render(
                    request, "update_contact.html", {"contact_form": contact_form}
                )

        contact_form = AddContactForm(instance=contact)
        return render(request, "update_contact.html", {"contact_form": contact_form})

    except contact.DoesNotExist:
        return HttpResponse("contact does not exist!!!")


def delete_contact(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return redirect("contact_list")
    except contact.DoesNotExist:
        return HttpResponse("contact does not exist!!!")
