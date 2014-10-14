# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413323347.909858
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/gallery.tmpl'
_template_uri = u'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'ui', context._clean_inheritance_tokens(), templateuri=u'crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'ui')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(ui.bar(crumbs)))
        __M_writer(u'\n')
        if title:
            __M_writer(u'    <h1>')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n')
        if post:
            __M_writer(u'    <p>\n        ')
            __M_writer(unicode(post.text()))
            __M_writer(u'\n    </p>\n')
        if folders:
            __M_writer(u'    <ul>\n')
            for folder, ftitle in folders:
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(folder))
                __M_writer(u'"><i\n        class="icon-folder-open"></i>&nbsp;')
                __M_writer(unicode(ftitle))
                __M_writer(u'</a></li>\n')
            __M_writer(u'    </ul>\n')
        if photo_array:
            __M_writer(u'    <ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(image['url']))
                __M_writer(u'" class="thumbnail image-reference" title="')
                __M_writer(unicode(image['title']))
                __M_writer(u'">\n                <img src="')
                __M_writer(unicode(image['url_thumb']))
                __M_writer(u'" alt="')
                __M_writer(unicode(image['title']))
                __M_writer(u'" /></a>\n')
            __M_writer(u'    </ul>\n')
        if site_has_comments and enable_comments:
            __M_writer(u'    ')
            __M_writer(unicode(comments.comment_form(None, permalink, title)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"130": 5, "143": 130, "22": 4, "25": 3, "31": 0, "52": 2, "53": 3, "54": 4, "59": 5, "64": 36, "70": 7, "88": 7, "89": 8, "90": 8, "91": 9, "92": 10, "93": 10, "94": 10, "95": 12, "96": 13, "97": 14, "98": 14, "99": 17, "100": 18, "101": 19, "102": 20, "103": 20, "104": 20, "105": 21, "106": 21, "107": 23, "108": 25, "109": 26, "110": 27, "111": 28, "112": 28, "113": 28, "114": 28, "115": 28, "116": 29, "117": 29, "118": 29, "119": 29, "120": 31, "121": 33, "122": 34, "123": 34, "124": 34}, "uri": "gallery.tmpl", "filename": "/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/gallery.tmpl"}
__M_END_METADATA
"""
