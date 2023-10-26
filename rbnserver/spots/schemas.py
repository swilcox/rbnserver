from ninja import ModelSchema
from .models import Spot


class SpotSchema(ModelSchema):
    class Config:
        model = Spot
        model_fields = "__all__"
