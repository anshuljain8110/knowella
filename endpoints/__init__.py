from fastapi import APIRouter
from endpoints.csv_reader import router as csv_reader
from endpoints.social import router as social
from endpoints.delivery_truck import router as truck_delivery

router = APIRouter(prefix="/api/v1")
router.include_router(csv_reader, tags=["Problem Statement 5 csv_reader"])
router.include_router(social, tags=["Problem Statement 10 Hot Posts"])
router.include_router(
    truck_delivery,
    tags=["Problem Statement 4 Truck Delivery"]
)
