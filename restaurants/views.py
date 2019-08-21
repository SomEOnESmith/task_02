from django.shortcuts import render

def test(request):
	context = {
	'msg': 'Hello World!',
	}
	return render(request, "test.html" , context)
