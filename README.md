# dj-svg

[![PyPI version](https://badge.fury.io/py/dj-svg.svg)](https://badge.fury.io/py/dj-svg)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/dj-svg.svg)](https://pypi.python.org/pypi/dj-svg/)
[![PyPI Supported Django Versions](https://img.shields.io/pypi/djversions/dj-svg.svg)](https://docs.djangoproject.com/en/dev/releases/)
[![GitHub Actions (Code quality and tests)](https://github.com/xshapira/dj-svg/workflows/Code%20quality%20and%20tests/badge.svg)](https://github.com/xshapira/dj-svg)

dj-svg is a fork of [django-inline-svg](https://github.com/mixxorz/django-inline-svg) which works with Django >5, it's a simple plugin that adds an `svg` template tag to inline your SVGs in your
Django templates.

## Installation

Install it from pypi.

```bash
pip install dj-svg
```

Add `dj_svg` to your `INSTALLED_APPS`.

```python
    INSTALLED_APPS = (
        ...
        'dj_svg',
        ...
    )
```

## Usage

Store your SVGs in folder named `svg` at the root of any of your static file
directories.

```bash
    my_app
    |-- static
    |   |-- svg
    |       |-- logo.svg
    |       |-- check.svg
    |       |-- cross.svg
```

Use the `svg` template tag.

```django
    {% load svg %}

    <h1 class="logo">{% svg 'logo' class="css-class" height="16" width="16" %}</h1>
```

You can set `SVG_DIRS` to control where to look for your svgs.

```python
    # settings.py

    SVG_DIRS=[
        os.path.join(BASE_DIR, 'my-svgs')
    ]
```

## Support

The tests are run against Django 4.0 to 5.0.4 on Python 3.8 to 3.12.

## License

MIT
