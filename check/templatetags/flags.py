from django import template

register = template.Library()


def format_flag_class(penyakit):
    return {
        'en': 'us',
        'ja': 'jp',
    }.get(penyakit, penyakit)

@register.inclusion_tag('flag.html')
def flag_by_penyakit(penyakit):

    flag_class = format_flag_class(penyakit)

    return {
        'name': penyakit,
        'class': flag_class
    }
