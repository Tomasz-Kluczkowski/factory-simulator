from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        fields = ', '.join(
            f'{field_name}={field_value}' for
            field_name, field_value in self.__dict__.items() if not field_name.startswith('_')
        )
        representation = f'<{self.__class__.__name__}({fields})>'

        return representation
