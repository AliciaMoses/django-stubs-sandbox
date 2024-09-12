from typing import reveal_type
from django import forms
from typing import Any

class Foo(forms.Form):
    foo_id = forms.IntegerField(
        required=True, label="Foo ID"
    )

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        reveal_type(cleaned_data)

        # Type of "cleaned_data" is "dict[str, Any]"Pylance
        # Revealed type is "Union[builtins.dict[builtins.str, Any], None]"
        
        return cleaned_data # Incompatible return value. Expected 'dict[str, Any]', got 'Union[dict[str, Any], None]'Pylance  / got dict[str, Any] | None, expected dict[str, Any]
    



