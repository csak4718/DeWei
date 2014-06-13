from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from polls.models import Poll

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5] # The negative sign in front of "-pub_date" indicates descending order. Ascending order is implied.
	context = {'latest_poll_list': latest_poll_list}
	#for poll in latest_poll_list: # poll is an object
	#	print poll.id # poll.id = 1
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	#print 'poll_id is:'
	#print poll_id
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
