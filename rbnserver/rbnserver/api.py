from ninja import NinjaAPI
from spots.api import router as spots_router

api = NinjaAPI(title="RBNServer", description="RBN Backend Server")

api.add_router("/spots/", spots_router)
