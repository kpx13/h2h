# -*- coding: utf-8 -*-

import os, sys, urllib
from instagram import client, subscriptions

sys.path.append(os.path.dirname(__file__) + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "h2h.settings")
from django.conf import settings
from django.core.files import File

from models import Instagallery

INSTAPI_CONFIG = {
    'client_id': '1f5f4f389fd044048b327e22f43a8e44',
    'client_secret': '8a4bfd1b733e4787aa1d032d554651c5'
}

# this allows output Russian characters to stdio
if sys.getdefaultencoding() != 'utf-8':
  reload(sys)
  sys.setdefaultencoding('utf-8')

def main(argv):
    instapi = client.InstagramAPI(**INSTAPI_CONFIG)

    max_id = None
    Instagallery.objects.all().update(processed=False)
    while True:
        media_pack, _ = instapi.user_recent_media(user_id='221216104', max_id=max_id)
        for media in media_pack:
            rec, created = Instagallery.objects.get_or_create(media_id=media.id)
            if created:
              img_low = urllib.urlretrieve(media.images['low_resolution'].url)
              img_std = urllib.urlretrieve(media.images['standard_resolution'].url)
              rec.image_low.save(media.id + "_306x306.jpg", File(open(img_low[0])))
              rec.image_std.save(media.id + "_640x640.jpg", File(open(img_std[0])))
            rec.link = media.link
            rec.likes_count = len(instapi.media_likes(media.id))
            if media.caption:
                rec.text = u''.join(uchar if uchar <= u'\uffff' else u'\ufffd' for uchar in media.caption.text)
            rec.processed = True
            rec.save()
        if len(media_pack) == 0:
            break
        max_id = media_pack[-1].id
    Instagallery.objects.filter(processed=False).delete()
    return 0

# main() sentinel
if __name__ == "__main__":
  sys.exit(main(sys.argv))
