from django.forms import widgets


class Input(widgets.Input):
    """
    Exists solely for overriding all inputs on Django forms at once
    """
    
    def __init__(self, attrs=None):
        extra_attrs = {"class": "form-control"}
        
        if attrs:
            extra_attrs.update(attrs)
        
        super(Input, self).__init__(extra_attrs)
        
    def render(self, name, value, attrs=None):
        from django.utils.encoding import force_unicode
        from django.utils.safestring import mark_safe
        from django.forms.util import flatatt

        if value is None:
            value = ''
            
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
            
        if self.is_required:
            final_attrs["required"] = "required"
        
        return mark_safe(u'<input%s />' % flatatt(final_attrs))


class TextInput(Input, widgets.TextInput):
    pass


class PasswordInput(TextInput):
    input_type = "password"
