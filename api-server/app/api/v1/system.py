from fastapi import APIRouter

from app.api.schema import SystemDetails, UpdateMachineName
from app.db.system import get_systems, update_machine_info

router = APIRouter(prefix="/system", tags=["System"])


@router.get("", response_model=SystemDetails)
def system_details():
    return get_systems()


@router.put("", response_model=SystemDetails, description="Mode: Sabha, Dining, GateIn, GateOut")
def update_machine_details(data: UpdateMachineName):
    update_machine_info(data)
    return get_systems()


@router.post('/reset')
def reset_machine():
    return {'message': 'Reset successful'}
