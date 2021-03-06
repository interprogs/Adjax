# 
# Adjax view API. These functions form the Adjax interface for Django views.
#

from adjax.base import get_store

def update(request, obj, attributes=None):
    """ Sends the updated version of the given attributes on the given object. 
        If no attributes are given, all attributes are sent (be careful if you
        don't want all data to be public).
        If a minus sign is in front of an attribute, it is omitted.
        A mix of attribtue names with and without minus signs is just silly.
        No other attributes will be included.
    """
    store = get_store(request)
    if not attributes or all(map(lambda s: s.startswith("-"), attributes)):
        attributes = obj.__dict__.keys()
    store.update(obj, (a for a in attributes if not a.startswith("-")))


def form(request, form_obj):
    """ Validate the given form and send errors to browser. """
    get_store(request).form(form_obj)


def replace(request, element=None, html=None, name=None, value=None):
    """ Replace the given DOM element with the given html. 
        The DOM element is specified using css identifiers.
        Some javascript libraries may have an extended syntax, 
        which can be used if you don't value portability.
    """
    get_store(request).replace(element, html, name, value)


def redirect(request, path):
    """ Redirect the browser dynamically to another page. """
    return get_store(request).redirect(path)


def hide(request, element=None, name=None):
    """ Hides the given DOM element.
        The DOM element is specified using css identifiers.
        Some javascript libraries may have an extended syntax, 
        which can be used if you don't value portability.
    """
    get_store(request).hide(element, name)


def extra(request, key, value):
    """ Send additional information to the browser. """
    get_store(request).extra(key, value)


def render(request, template_name, context=None, prefix=None):
    """ Update any included templates. """
    get_store(request).render_to_response(template_name, context, prefix)

# For backwards compatibility, this is the old name 
render_to_response = render


def response(request, include_messages=False):
    """ Provide an appropriate HTTP response. """
    return get_store(request).response(include_messages=include_messages)
