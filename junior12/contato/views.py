from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from junior12.contato.forms import ContactForm

class ContactView(FormView):
    template_name = 'frontend/contato.html'
    form_class = ContactForm
    success_url = '/contato/sucesso/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)

contact_success = TemplateView.as_view(
    template_name='frontend/contato_sucesso.html'
)