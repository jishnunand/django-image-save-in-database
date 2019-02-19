from django import template

register = template.Library()

@register.simple_tag
def decode(value):
	img_val = value.decode('UTF-8')
	img = "data:image/png;base64, %s" %img_val
	return img
