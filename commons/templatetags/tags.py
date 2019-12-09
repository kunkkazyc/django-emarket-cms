from django import template
from datetime import datetime
from django.contrib.admin.templatetags import admin_list
from django.db.models.query import RawQuerySet
from django.contrib.admin.views.main import SEARCH_VAR

register = template.Library()


@register.filter
def format_time(value):
    try:
        time_int = int(value) / 1000
        time_str = datetime.fromtimestamp(time_int).strftime('%H:%M:%S')
        return time_str
    except ValueError:
        return ''


@register.filter
def format_date(value):
    try:
        time_int = int(value) / 1000
        time_str = datetime.fromtimestamp(time_int).strftime('%Y-%m-%d')
        return time_str
    except ValueError:
        return ''


@register.filter
def format_full_datetime(value):
    try:
        time_int = int(value) / 1000
        time_str = datetime.fromtimestamp(time_int).strftime('%Y-%m-%d %H:%M:%S')
        return time_str
    except ValueError:
        return ''


@register.filter
def format_date_time(value):
    try:
        time_int = int(value) / 1000
        time_str = datetime.fromtimestamp(time_int).strftime('%m.%d %H:%M')
        return time_str
    except ValueError:
        return ''


@register.filter
def format_mils2minute(value):
    try:
        time_int = int(value) * 1.0 / (60 * 1000)
        return str("%.2f" % time_int)
    except ValueError:
        return ''


@register.filter
def length(obj):
    if isinstance(obj, RawQuerySet):
        return len(list(obj))
    return len(obj)


# @register.filter
# def parse_recording_type(type_id):
#     return RecordingType.get_name(type_id)
#
#
# @register.filter
# def parse_media_type(media_type):
#     return MediaType.get_name(media_type)
#
#
# @register.filter
# def parse_bool_status(bool_code):
#     return BoolType.get_str(bool_code)
#
#
# @register.filter
# def parse_course_type(app_id):
#     return CourseType.get_name(app_id)
#
#
# @register.filter
# def parse_label_input_type(input_type):
#     return LabelInputType.get_name(input_type)


@register.filter
def format_material_file_name(name):
    names = name.split(".")
    fmf_len = len(names[1])
    part1 = name[0:2]
    part2 = name[-(fmf_len + 3):]
    return part1 + "..." + part2


# @register.filter
# def parse_episode_set_type(episode_set_type):
#     return EpisodeSetType.parse(episode_set_type)


@register.inclusion_tag("admin/cms/Lecture/label_detail.html")
def label_detail(value, arg, selected):
    return {'category': arg, 'cate_list': value[arg.id], 'selected': selected,}


@register.inclusion_tag("admin/cms/Lecture/change_list_results.html")
def custom_result_list(cl):
    headers = list(admin_list.result_headers(cl))
    num_sorted_fields = 0
    for h in headers:
        if h['sortable'] and h['sorted']:
            num_sorted_fields += 1
    return {
        'cl': cl,
        'result_hidden_fields': list(admin_list.result_hidden_fields(cl)),
        'result_headers': headers,
        'num_sorted_fields': num_sorted_fields,
        'results': list(admin_list.results(cl))}


# modified by lirun
# date: 20160130
@register.inclusion_tag('admin/cms/Lecture/lecture_actions.html', takes_context=True)
def admin_actions_top(context):
    context['action_index'] = context.get('action_index', -1) + 1
    context['is_top'] = True
    return context


@register.inclusion_tag('admin/cms/Lecture/actions.html', takes_context=True)
def admin_actions_bottom(context):
    context['action_index'] = context.get('action_index', -1) + 1
    context['is_top'] = False
    return context


@register.inclusion_tag('admin/cms/Lecture/episode/episode_set.html')
def episode_list(episode_set, overlap_episodes, lecture):
    return {"episode_set": episode_set, "overlap_episodes": overlap_episodes, "lecture": lecture}


@register.inclusion_tag('admin/cms/LectureTemplate/episode_set.html')
def episode_set_template_list(episode_set, lecture):
    return {"episode_set": episode_set, "lecture": lecture,}


@register.filter
def format_file_length(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10

    for s in reversed(symbols):
        if n >= prefix[s]:
            value = int(float(n) / prefix[s])
            return '%s%s' % (value, s)
    return '%sB' % n


@register.filter
def convert_to_api_prefix(app):
    if app == "cms":
        return "gwy"
    return app


@register.filter
def convert_to_api_prefix(app_label):
    if app_label == "cms":
        return "gwy"
    return app_label


@register.filter
def format_group_name(group_name):
    if group_name == "cms":
        return "gwy"
    return group_name


# @register.filter
# def parse_episode_question_status(status):
#     return EpisodeTikuStatus.get_name(status)


@register.inclusion_tag('admin/search_form.html', takes_context=True)
def advanced_search_form(context, cl):
    """
    Displays a search form for searching the list.
    """
    return {
        'asf': context.get('asf'),
        'cl': cl,
        'show_result_count': cl.result_count != cl.full_result_count,
        'search_var': SEARCH_VAR}


# @register.filter
# def parse_user_answer_status(status):
#     return UserExerciseStatus.get_name(status)
#
#
# @register.inclusion_tag("admin/tags/express_type_tag.html")
# def express_type_choices(type_id):
#     express_types = ExpressType.CHOICES[1:]
#     choices = [{"value": express_type[0], "name": express_type[1]} for express_type in
#                express_types]
#     return {
#         "choices": choices,
#         "type_id": type_id
#     }
#
#
# @register.inclusion_tag("admin/tags/benefits_tag.html")
# def benefits_choices():
#     benefits_types = ContentBizType.CHOICES
#     choices = [{"value": t[0], "name": t[1]} for t in benefits_types]
#     return {"choices": choices}
#
#
# @register.filter
# def parse_content_type(type_id):
#     return ContentType.get_name(type_id)
#
#
# @register.filter
# def parse_content_model_name(content_type):
#     if content_type == ContentType.KE:
#         return "lecture"
#     if content_type == ContentType.GUIDE:
#         return "guidecontent"
#     if content_type == ContentType.SPU:
#         return "lecturespu"


@register.filter
def format_to_five_score(value):
    return int(value / 2)
