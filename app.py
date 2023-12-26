from fastapi import Depends, FastAPI, Body, HTTPException

from database.db import User, get_async_session
from database.schemas import UserCreate, UserRead, UserUpdate, PropertyUpdate
from database.users import auth_backend, current_active_user, fastapi_users
from database import queries

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/properties/")
async def get_all_properties(session=Depends(get_async_session)):
    return await queries.get_all_properties(session)


@app.post("/properties/add/")
async def add_property(property_title: str = Body(),
                       property_description: str = Body(),
                       property_address: str = Body(),
                       user=Depends(current_active_user),
                       session=Depends(get_async_session)):
    owner_id = user.id
    property_id = await queries.add_property(property_title, property_description, property_address, owner_id, session)
    return {"id": property_id}


@app.patch("/properties/{property_id}/update/")
async def update_property(property_id: int,
                          property_update: PropertyUpdate,
                          user=Depends(current_active_user),
                          session=Depends(get_async_session)):
    property = await queries.get_property(property_id, session)
    if not property:
        raise HTTPException(status_code=404, detail="PROPERTY_NOT_FOUND")
    if not property.owner_id == user.id:
        raise HTTPException(status_code=403, detail="PROPERTY_CAN_ONLY_BE_UPDATED_BY_OWNER_OR_ADMIN")
    await queries.update_property(session,
                                  property_id,
                                  **property_update.model_dump(exclude_unset=True))
    return {"id": property_id}


@app.delete("/properties/{property_id}/delete/")
async def delete_property(property_id: int,
                          user=Depends(current_active_user),
                          session=Depends(get_async_session)):
    property = await queries.get_property(property_id, session)
    if not property:
        raise HTTPException(status_code=404, detail="PROPERTY_NOT_FOUND")
    if not property.owner_id == user.id:
        raise HTTPException(status_code=403, detail="PROPERTY_CAN_ONLY_BE_DELETED_BY_OWNER_OR_ADMIN")
    await queries.delete_property(property_id, session)
    return {"id": property_id}
