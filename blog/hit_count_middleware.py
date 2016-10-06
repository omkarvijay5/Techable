from blog.models import Hit

class HitCounter(object):

    def process_request(self, request):
        if request.session.session_key is None:
            # get the user ip address
            ip = request.META.get('REMOTE_ADDR')
            request.session.save()
            hitcount, created = Hit.objects.get_or_create(ip=ip)
            hitcount.count += 1
            hitcount.save()
        return None
