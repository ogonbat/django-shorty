from django.conf import settings

SHORTY_MODERATE = getattr(settings, 'SHORTY_MODERATE', False)
SHORTY_ANONYMOUS_ADD = getattr(settings, 'SHORTY_ANONYMOUS_ADD', False)
SHORTY_BANNED = getattr(settings, 'SHORTY_BANNED', '/banned')
SHORTY_PENDING = getattr(settings, 'SHORTY_PENDING', '/pending')
SHORTY_REFUSED = getattr(settings, 'SHORTY_REFUSED', '/refused')