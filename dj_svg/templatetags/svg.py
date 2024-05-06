import logging
import os
import pathlib

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.exceptions import ImproperlyConfigured
from django.utils.safestring import mark_safe

from dj_svg.exceptions import SVGNotFound

logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def svg(filename, *args, **kwargs):
    SVG_DIRS = getattr(settings, "SVG_DIRS", [])

    if not isinstance(SVG_DIRS, list):
        raise ImproperlyConfigured("SVG_DIRS setting must be a list")

    path = None

    if SVG_DIRS:
        for directory in SVG_DIRS:
            svg_path = os.path.join(directory, f"{filename}.svg")

            if os.path.isfile(svg_path):
                path = svg_path
    else:
        path = finders.find(os.path.join("svg", f"{filename}.svg"), all=True)

    if not path:
        message = f"SVG '{filename}.svg' not found"

        # Raise exception if DEBUG is True, else just log a warning.
        if settings.DEBUG:
            raise SVGNotFound(message)
        logger.warning(message)
        return ""

    # Sometimes path can be a list/tuple if there's more than one file found
    if isinstance(path, (list, tuple)):
        path = path[0]

    svg = pathlib.Path(path).read_text()
    if kwargs:
        attributes = " ".join([f'{k}="{v}"' for k, v in kwargs.items()])
        svg = svg.replace("<svg", f"<svg {attributes}")

    return mark_safe(svg)
