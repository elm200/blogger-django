from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator

from entries.models import Entry
from entries.forms import EntryForm

entries_per_page = 3

def index(request):
    entries = Entry.objects.order_by('-created_at')
    paginator = Paginator(entries, entries_per_page)
    entries= paginator.page(request.GET.get('page', 1))
    context = { 'entries': entries, 'title': 'エントリー一覧' }
    return render(request, 'entries/index.html', context)

def show(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    context = { 'entry': entry, 'title': 'エントリー詳細' }
    return render(request, 'entries/show.html', context)

def new(request):
    entry = Entry()
    form = EntryForm()
    context = { 'entry': entry, 'title': 'エントリー新規作成', 'form': form }
    return render(request, 'entries/new.html', context)

def create(request):
    entry = Entry(title=request.POST['title'], body=request.POST['body'])
    entry.save()

    return HttpResponseRedirect(reverse("show", args=(entry.id,)))

def edit(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    form = EntryForm()
    context = { 'entry': entry, 'title': 'エントリー編集', 'form': form }
    return render(request, 'entries/edit.html', context)

def update(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)

    entry.title = request.POST['title']
    entry.body = request.POST['body']
    entry.save()

    return HttpResponseRedirect(reverse("show", args=(entry.id,)))

def destroy(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.delete()
    return HttpResponse(status=204)

def create_comment(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.comment_set.create(user_name=request.POST['user_name'], body=request.POST['comment_body'])
    return HttpResponseRedirect(reverse("show", args=(entry.id,)))
