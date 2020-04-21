from .base import *
from .base import env
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="akxYonIXwKWIMJIncDbnqqjOjGqvDyXkp5riBS7NUGTBNF1x2IXyjzj1xp4f65XX",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER", default="no") == "yes":
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
INSTALLED_APPS += ["django_extensions", "drf_yasg"]
try:
    from .local_settings import *
except ImportError:
    pass
