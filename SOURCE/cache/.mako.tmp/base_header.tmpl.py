# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413323347.817167
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/base_header.tmpl'
_template_uri = u'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links', 'html_translation_header', 'html_header', 'html_site_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <nav id="menu" role="navigation">\n    <ul>\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer(u'            <li> ')
                __M_writer(unicode(text))
                __M_writer(u'\n            <ul>\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(permalink))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a></li>\n')
                    else:
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a></li>\n')
                __M_writer(u'            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(permalink))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
                else:
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
        __M_writer(u'    ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n    </ul>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'        <div id="toptranslations">\n            <h2>')
            __M_writer(unicode(messages("Languages:")))
            __M_writer(u'</h2>\n            ')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_translation_header():
            return render_html_translation_header(context)
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer(u'\n    <header id="header" role="banner">\n        ')
        __M_writer(unicode(html_site_title()))
        __M_writer(u'\n        ')
        __M_writer(unicode(html_translation_header()))
        __M_writer(u'\n        ')
        __M_writer(unicode(html_navigation_links()))
        __M_writer(u'\n')
        if search_form:
            __M_writer(u'            <div class="searchform" role="search">\n                ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n            </div>\n')
        __M_writer(u'    </header>\n    ')
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <h1 id="brand"><a href="')
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'" title="')
        __M_writer(unicode(blog_title))
        __M_writer(u'" rel="home">\n')
        if logo_url:
            __M_writer(u'        <img src="')
            __M_writer(unicode(logo_url))
            __M_writer(u'" alt="')
            __M_writer(unicode(blog_title))
            __M_writer(u'" id="logo">\n')
        __M_writer(u'\n')
        if show_blog_title:
            __M_writer(u'        <span id="blog-title">')
            __M_writer(unicode(blog_title))
            __M_writer(u'</span>\n')
        __M_writer(u'    </a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 2, "25": 0, "32": 2, "33": 16, "34": 28, "35": 57, "36": 66, "42": 30, "55": 30, "56": 33, "57": 34, "58": 35, "59": 35, "60": 35, "61": 37, "62": 38, "63": 39, "64": 39, "65": 39, "66": 39, "67": 39, "68": 40, "69": 41, "70": 41, "71": 41, "72": 41, "73": 41, "74": 44, "75": 45, "76": 46, "77": 47, "78": 47, "79": 47, "80": 47, "81": 47, "82": 48, "83": 49, "84": 49, "85": 49, "86": 49, "87": 49, "88": 53, "89": 53, "90": 53, "91": 54, "92": 54, "98": 59, "108": 59, "109": 60, "110": 61, "111": 62, "112": 62, "113": 63, "114": 63, "120": 4, "134": 4, "135": 6, "136": 6, "137": 7, "138": 7, "139": 8, "140": 8, "141": 9, "142": 10, "143": 11, "144": 11, "145": 14, "146": 15, "147": 15, "153": 18, "163": 18, "164": 19, "165": 19, "166": 19, "167": 19, "168": 20, "169": 21, "170": 21, "171": 21, "172": 21, "173": 21, "174": 23, "175": 24, "176": 25, "177": 25, "178": 25, "179": 27, "185": 179}, "uri": "base_header.tmpl", "filename": "/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/base_header.tmpl"}
__M_END_METADATA
"""
