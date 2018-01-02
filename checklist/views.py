from django.shortcuts import render

from checklist.models import ListTemplate, List, ListItemTemplate, Item


def home(request):
    if request.method == 'GET':
        list_templates = ListTemplate.objects.all()
        return render(request, 'checklist/home.html', {'list_templates': list_templates})
    if request.method == 'POST':
        list_template_id = request.POST['list-templates']
        new_list = List.objects.create(
            name='checklist test'
        )
        template_items = ListItemTemplate.objects.filter(list__id=list_template_id)
        # new_items = new_list.item_set
        print(new_list)
        for item in template_items:
            Item.objects.create(
                name=item.name,
                list=new_list
            )

        new_list.save()

        return render(request, 'checklist/create_checklist.html')


def create(request):
    return render(request, 'checklist/create_checklist.html')
