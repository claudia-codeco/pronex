# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1413323347.921455
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/story.tmpl'
_template_uri = u'story.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'pheader', context._clean_inheritance_tokens(), templateuri=u'post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pheader')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pheader = _mako_get_namespace(context, 'pheader')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<article class="storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <header>\n        ')
        __M_writer(unicode(pheader.html_title()))
        __M_writer(u'\n        ')
        __M_writer(unicode(pheader.html_translations(post)))
        __M_writer(u'\n    </header>\n    <div itemprop="articleBody text">\n    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    </div>\n')
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            __M_writer(u'        <section class="comments">\n        <h2>')
            __M_writer(unicode(messages("Comments")))
            __M_writer(u'</h2>\n        ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer(u'\n        </section>\n')
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if post.meta('keywords'):
            __M_writer(u'        <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="author" content="')
        __M_writer(unicode(post.author()))
        __M_writer(u'">\n    ')
        __M_writer(unicode(helper.open_graph_metadata(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.meta_translations(post)))
        __M_writer(u'\n')
        if post.description():
            __M_writer(u'        <meta name="description" itemprop="description" content="')
            __M_writer(unicode(post.description()))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 17, "129": 17, "135": 129, "22": 3, "25": 4, "28": 2, "34": 0, "51": 2, "52": 3, "53": 4, "54": 5, "59": 19, "64": 37, "70": 21, "82": 21, "83": 24, "84": 24, "85": 25, "86": 25, "87": 28, "88": 28, "89": 30, "90": 31, "91": 32, "92": 32, "93": 33, "94": 33, "95": 36, "101": 7, "110": 7, "111": 8, "112": 8, "113": 9, "114": 10, "115": 10, "116": 10, "117": 12, "118": 12, "119": 12, "120": 13, "121": 13, "122": 14, "123": 14, "124": 15, "125": 15, "126": 16, "127": 17}, "uri": "story.tmpl", "filename": "/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/story.tmpl"}
__M_END_METADATA
"""
