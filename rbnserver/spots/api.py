import json
import uuid
from django.shortcuts import get_object_or_404
from ninja import Router, Query
from ninja.pagination import paginate
from .models import Spot
from .schemas import SpotSchema, SpotFilterSchema
from .tasks import add_spot_task

router = Router()


@router.get("/", response=list[SpotSchema])
@paginate
def list_spots(request, filters: SpotFilterSchema = Query(...)):
    q = filters.get_filter_expression()
    return Spot.objects.filter(q)


@router.get("/{spot_id}", response=SpotSchema)
def spot_details(request, spot_id: uuid.UUID):
    """return a single spot record"""
    return get_object_or_404(Spot, id=spot_id)


@router.post("/")
def spot_add(request, payload: SpotSchema):
    """background task oriented add"""
    data = {"payload": json.loads(payload.json())}
    # assign a UUID to it if not present for idempotent handling...
    id = data["payload"].get("id") or str(uuid.uuid4())
    data["payload"]["id"] = id
    add_spot_task.send_with_options(kwargs=data)
    return {"id": id}
