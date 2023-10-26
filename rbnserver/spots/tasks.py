from time import sleep
import dramatiq

from .models import Spot
from .schemas import SpotSchema


@dramatiq.actor(max_retries=1)
def add_spot_task(payload: SpotSchema):
    """
    function that actually adds a spot and any additional stats loading
    """
    new_spot_data = SpotSchema(**payload)
    print(new_spot_data)
    # this would be the area where we'd add even more stats collection
    # or longer / more complex calculations
    # also optional filtering of spots we don't want to save
    spot = Spot.objects.get_or_create(**new_spot_data.dict())
    # additional background tasks or calls to tasks go here
