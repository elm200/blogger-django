from django.shortcuts import get_object_or_404, render
from .models import Entry

def index(request):
    entries = Entry.objects.order_by('-created_at')
    context = { 'entries': entries, 'title': 'エントリー一覧' }
    return render(request, 'entries/index.html', context)

def show(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    context = { 'entry': entry, 'title': 'エントリー詳細' }
    return render(request, 'entries/show.html', context)
