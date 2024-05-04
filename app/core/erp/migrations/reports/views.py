from django.views.generic import TemplateView


# Create your views here.
class ReportChequeView(TemplateView):
    template_name = 'cheque/report.html'
