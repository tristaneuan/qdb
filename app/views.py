from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView

from app.forms import QuoteForm
from app.models import Quote, Tag


def index(request):
    quote_list = Quote.objects.all().order_by('-date')[:5]
    context = {'quote_list': quote_list}
    return render(request, 'app/index.html', context)


def detail(request, quote_id):
    q = get_object_or_404(Quote, pk=quote_id)
    context = {'quote': q}
    return render(request, 'app/detail.html', context)


def tag(request, tag_id):
    t = get_object_or_404(Tag, pk=tag_id)
    context = {'tag': t}
    return render(request, 'app/tag.html', context)


class QuoteCreate(CreateView):
    template_name = 'app/quote_create.html'
    form_class = QuoteForm
    model = Quote

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super(QuoteCreate, self).form_valid(form)
