from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .forms import ImageForm, PlantCreationForm
from .models import Image
from .models import Plant

@login_required
def plant(request):

	ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

	if request.method == 'POST':

		plantForm = PlantCreationForm(request.POST)
		formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

		if plantForm.is_valid() and formset.is_valid():
			plant_form = plantForm.save(commit=False)
			plant_form.save()

			for form in formset.cleaned_data:
				#Stops from crashing if a user doesn't upload all photos
				if form:
					image = form['image']
					photo = Image(plant=plant_form, image=image)
					photo.save()
			else:
				print(plantForm.errors, formset.errors)
		messages.success(request, "Upload successful")
		return HttpResponseRedirect("/")
	else:
		plantForm = PlantCreationForm()
		formset = ImageFormSet(queryset=Image.objects.none())
	return render(request, 'plant/new_plant_form.html', {'plantForm': plantForm, 'formset': formset})

class PlantListView(ListView):
	model = Plant
	template_name = 'plant/plant_list.html'
	context_object_name = 'plants'