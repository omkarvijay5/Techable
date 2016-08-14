from .base import *

AWS_STORAGE_BUCKET_NAME = 'techable-storages'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'blog.custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'blog.custom_storages.MediaStorage'


STATICFILES_LOCATION = 'static'
# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
