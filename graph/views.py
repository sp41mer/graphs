import json

from django.shortcuts import render
from django.views.generic import TemplateView
from models import Student
# Create your views here.

class IndexListView(TemplateView):
    template_name = "graph/index.html"


    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        nodes = [{'id': student.name, 'group': student.group} for student in students]
        print nodes
        links = []
        already_made = []
        for student in students:
            for friend in student.friends.all():
                if friend not in already_made:
                    links.append({'source': student.name, "target": friend.name, "value": 1})
            already_made.append(student)
        dict = {"nodes": nodes, "links": links}
        with open('graph/static/graph/js/data/data.json', 'w') as outfile:
            json.dump(dict, outfile, indent=4, sort_keys=True, separators=(',', ':'))
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)