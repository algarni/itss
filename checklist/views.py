from django.shortcuts import render, redirect

from checklist.models import ListTemplate, List, ListItemTemplate, Item


def home(request):
    checklists = List.objects.all()
    list_templates = ListTemplate.objects.all()
    if request.method == 'GET':
        return render(request, 'checklist/home.html', {
            'list_templates': list_templates,
            'checklists': checklists
        })
    if request.method == 'POST':
        title = request.POST['title']
        list_template_id = request.POST['list-templates']
        new_list = List.objects.create(
            name=title
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

        return redirect(checklist_detail, pk=new_list.pk)


def checklist_detail(request, pk):
    checklist = List.objects.get(pk=pk)
    items = Item.objects.filter(list__id=pk)
    return render(request, 'checklist/checklist_detail.html',
                  {'items': items, 'checklist':checklist})
