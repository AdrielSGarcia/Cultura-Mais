from django.shortcuts import render
from django.views.generic import TemplateView


class VueAppView(TemplateView):
    """View para servir a aplicação Vue.js"""
    template_name = 'vue_base.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cultura Mais - Portal Cultural'
        return context
