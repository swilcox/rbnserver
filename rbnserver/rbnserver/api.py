from ninja import NinjaAPI
from spots.api import router as spots_router

api = NinjaAPI()

api.add_router("/spots/", spots_router)
