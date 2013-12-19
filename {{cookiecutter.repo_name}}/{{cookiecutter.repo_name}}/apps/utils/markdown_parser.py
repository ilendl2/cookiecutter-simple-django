import markdown
import re
from markdown.inlinepatterns import IMAGE_REFERENCE_RE, REFERENCE_RE

from flatpages_x.models import FlatPageImage
from filer.models import File
from django.core.exceptions import ObjectDoesNotExist
img_ref_re = re.compile(IMAGE_REFERENCE_RE)
reference_re = re.compile(REFERENCE_RE)
pdf_doc_pattern = r'^.*\.(doc|DOC|pdf|PDF)'

from markdown.inlinepatterns import ImagePattern, LinkPattern



def parse(text):
    """
    This is a test of md references

    ![Alt text 2][1]

    >>> parse('![Alt text 2][1]')
    u'<p><img alt="Alt text 2" src="/site_media/media/flatpage/2013/01/22/bottom-left2.gif" /></p>'



    """
    md = markdown.Markdown(['codehilite', 'tables', ])

    for iref in re.findall(img_ref_re, text):
        img_id = iref[7]
        try:
            image = FlatPageImage.objects.get(pk=int(img_id))
            md.references[img_id] = (image.image_path.url, '')
        except ObjectDoesNotExist:
            pass

    for lref in re.findall(reference_re, text):
        doc_name = lref[7]
        try:
            doc = File.objects.get(name=doc_name)
            md.references[doc_name]= (doc.url, doc.name)
        except ObjectDoesNotExist:
            pass

    return md.convert(text)

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    #print parse('![Alt text 1][1]')
    print parse('[an example] [id] ')

