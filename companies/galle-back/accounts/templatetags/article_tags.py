import math
from django import template

register = template.Library()


@register.assignment_tag
def get_number_of_sliders(article_list):
	count = len(article_list)
	no_of_sliders = int(math.ceil(count / 4.0))
	return range(1, no_of_sliders+1)

@register.assignment_tag
def slider_articles(slide_no, article_list):
	return article_list[(slide_no-1)*4:(slide_no-1)*4+4]
