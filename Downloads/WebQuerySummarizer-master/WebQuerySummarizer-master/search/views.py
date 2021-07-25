from django.shortcuts import render
from django.shortcuts import redirect
from ui.forms import NameForm
# Create your views here.
def searchQuery(request):
    #search query and get links on the first page
    #prepare links.txt file and save it
    # if this is a POST request we need to process the form data
        # create a form instance and populate it with data from the request:
    form = NameForm(request.POST)
    print("test1")
    # check whether it's valid:
    if form.is_valid():
        query = form.cleaned_data['queryy']
        print(query)

        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        return redirect(to='/scrape/'+query)

    # if a GET (or any other method) we'll create a blank form
