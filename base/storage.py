from datetime import datetime

from uuid import uuid4
from base64 import urlsafe_b64encode


def uuid():
    """
    Why use UUIDs as upload paths?
        Link: https://pypi.python.org/pypi/django-uuid-upload-path/1.0.0
        Django tries to ensure that all your uploaded files are given unique names on the filesystem. It
        does this by checking if a file with the same name exists before saving a new one, and adding a
        suffix if the new file would otherwise conflict with the existing one. If you are saving files to
        disk using the built-in django.core.files.storage.FileSystemStorage, this isnt much of a problem.
        However, if you're using a cloud file storage, such as storages.backends.s3boto.S3BotoStorage, this
        uniqueness check can have a noticeable effect on the performance of file uploads. Worse, the default
        configuration of S3BotoStorage is to overwrite existing files with the same name when uploading a new file!
        By generating a unique filename for each uploaded file, django-uuid-upload-path removes the need for a costly
        uniqueness check, and avoids accidentally overwriting existing files on remote cloud storages.
    It will generate the string of ( like etc: '3x2LRbdHSa29vLzdhgKsvg') length 22.
    return string (etc: 3x2LRbdHSa29vLzdhgKsvg)
    """
    return urlsafe_b64encode(uuid4().bytes).decode("ascii").rstrip("=")


def upload_image(instance, image):
    """
    Stores the attachment in a "per tech-gallery/module-type/yyyy/mm/dd" folder.
    :param instance, filename
    :param image
    :returns ex: tech-gallery/image/2016/03/30-3x2LRbdHSa29vLzdhgKsvg/filename
    """
    today = datetime.today()
    return 'tech-gallery/{model}/{year}/{month}/{day}/{uuid}-{image}'.format(
        model=instance._meta.model_name,
        year=today.year,
        month=today.month,
        day=today.day,
        uuid=uuid(),
        image=image
)
