from django import template

register = template.Library()

@register.filter
def add_class(form_field, class_name):
    if hasattr(form_field, 'field'):
        # Applique la classe à l'objet formulaire (Field)
        return form_field.as_widget(attrs={'class': class_name})
    return form_field
