from datetime import datetime
from typing import Optional
from ninja import ModelSchema, FilterSchema, Field
from .models import Spot


class SpotSchema(ModelSchema):
    """Standard Spot Schema"""

    class Config:
        model = Spot
        model_fields = "__all__"


class SpotFilterSchema(FilterSchema):
    """Schema for Querying Spots"""

    calling_station: Optional[str]
    receiving_station: Optional[str]
    received_since: Optional[datetime] = Field(q="ts__gt")
