from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.template import RequestContext
from django.conf import settings
import os

class Render:
    def fetch_resources(uri, rel):
        if uri.startswith(sUrl):
            sUrl = settings.STATIC_URL
            sRoot = settings.STATIC_ROOT
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
            return path

    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response, link_callback=fetch_resources)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)
