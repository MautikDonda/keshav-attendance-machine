import datetime

from fastapi import APIRouter
from starlette.responses import Response

from app.api.schema import ExternalUser
from app.db.external_user import get_users, get_user_by_id, add_user

router = APIRouter(prefix="/external-users", tags=["External Users"])


@router.get("", response_model=list[ExternalUser])
def list_external_entities():
    return get_users()


@router.get("/download")
def download_external_user():
    users = get_users()
    headers = 'Id, DisplayId, FirstName, LastName, CardNumber'
    content = headers + '\n'
    for record in users:
        content += f"{record.id}, {record.display_id}, {record.first_name}, {record.last_name}, {record.card_number}\n"
    response = Response(content=content.encode('utf8'), status_code=200)
    response.headers["Content-Disposition"] = \
        f"attachment; filename=External_Users_{datetime.datetime.now().isoformat()}.csv"
    response.headers["Content-Type"] = "application/octet-stream"
    return response


@router.get("/{uid}", response_model=ExternalUser)
def get_external_user(uid: str):
    return get_user_by_id(uid)


@router.post("", response_model=ExternalUser, status_code=201)
def create_external_user(data: ExternalUser):
    return add_user(data)

