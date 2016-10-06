from blog.services import increment_hit_count


class HitCounter(object):

    def process_request(self, request):
        if request.session.session_key is None:
            # get the user ip address
            ip = request.META.get('REMOTE_ADDR')
            request.session.save()
            increment_hit_count(ip)
        return None
