from django import forms

from .models import Profesores, Curso
class AsignacionForm(forms.ModelForm):
#todos los campos de Evento
    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion', 'profesores')
        def __init__ (self, *args, **kwargs):
            super(AsignacionForm, self).__init__(*args, **kwargs)
            self.fields["profesores"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["profesores"].help_text = "Ingrese los actores que asistiran al evento"
            self.fields["profesores"].queryset = Persona.objects.all()
