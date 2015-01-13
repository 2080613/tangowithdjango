from django.http import HttpResponse

def index(request):
    return HttpResponse("""<p>Rango says hey there world!</ p>
    <p>A link to the <a href=\"/rango/about\">about</ a> page.</ p>""")

def about(request):
    return HttpResponse("""<p>This tutorial has been put together by Seoras Macdonald,
     2080613</ p><p>A link to the <a href=\"/rango\">index</ a> page.</ p>""")