import asyncio
from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.exceptions import ServiceException
from app.schemas import (
    ClassroomModel,
    ClassroomPostModel,
    ClassroomUpdateModel,
    SchoolModel,
    SchoolPostModel,
    SchoolUpdateModel,
    UserAccountModel,
    UserAccountPostModel,
    UserAccountUpdateModel,
)
from app.services import (
    ClassroomService,
    SchoolService,
    ServiceDependency,
    UserAccountService,
)

# Routers
school_router = APIRouter(
    prefix="/school", tags=["school"], responses={404: {"description": "Not Found"}}
)


classroom_router = APIRouter(
    prefix="/classroom",
    tags=["classroom"],
    responses={404: {"description": "Not Found"}},
)


user_router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "Not Found"}}
)


# Routes
# List
@school_router.get("/")
async def list_schools(
    ids: Annotated[Optional[int], Query(alias="schools")] = None,
    service: SchoolService = Depends(ServiceDependency("SchoolService")),
) -> List[SchoolModel]:
    return await asyncio.to_thread(service.get_list, ids)


@classroom_router.get("/")
async def list_classrooms(
    ids: Annotated[Optional[int], Query(alias="classrooms")] = None,
    service: ClassroomService = Depends(ServiceDependency("ClassroomService")),
) -> List[ClassroomModel]:
    return await asyncio.to_thread(service.get_list, ids)


@user_router.get("/")
async def list_users(
    ids: Annotated[Optional[int], Query(alias="users")] = None,
    service: UserAccountService = Depends(ServiceDependency("UserAccountService")),
) -> List[UserAccountModel]:
    return await asyncio.to_thread(service.get_list, ids)


# Read
@school_router.get("/{id}")
async def get_school(
    id: int, service: SchoolService = Depends(ServiceDependency("SchoolService"))
) -> SchoolModel:
    result = await asyncio.to_thread(service.get, id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Not found.")


@classroom_router.get("/{id}")
async def get_classroom(
    id: int, service: ClassroomService = Depends(ServiceDependency("ClassroomService"))
) -> ClassroomModel:
    result = await asyncio.to_thread(service.get, id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Not found.")


@user_router.get("/{id}")
async def get_user(
    id: int,
    service: UserAccountService = Depends(ServiceDependency("UserAccountService")),
) -> UserAccountModel:
    result = await asyncio.to_thread(service.get, id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Not found.")


# Create
@school_router.post("/")
async def create_school(
    data: SchoolPostModel,
    service: SchoolService = Depends(ServiceDependency("SchoolService")),
) -> SchoolModel:
    try:
        result = await asyncio.to_thread(service.create, data)
        return result
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Could not create. Contact the administrator."
        )


@classroom_router.post("/")
async def create_classroom(
    data: ClassroomPostModel,
    service: ClassroomService = Depends(ServiceDependency("ClassroomService")),
) -> ClassroomModel:
    try:
        result = await asyncio.to_thread(service.create, data)
        return result
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Could not create. Contact the administrator."
        )


@user_router.post("/")
async def create_user(
    data: UserAccountPostModel,
    service: UserAccountService = Depends(ServiceDependency("UserAccountService")),
) -> UserAccountModel:
    try:
        result = await asyncio.to_thread(service.create, data)
        return result
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Could not create. Contact the administrator."
        )


# Update
@school_router.patch("/{id}")
async def update_school(
    id: int,
    data: SchoolUpdateModel,
    service: SchoolService = Depends(ServiceDependency("SchoolService")),
) -> SchoolModel:
    try:
        result = await asyncio.to_thread(service.update, id, data)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Not found.")
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Could not update. Contact the administrator."
        )


@classroom_router.patch("/{id}")
async def update_classroom(
    id: int,
    data: ClassroomUpdateModel,
    service: ClassroomService = Depends(ServiceDependency("ClassroomService")),
) -> ClassroomModel:
    try:
        result = await asyncio.to_thread(service.update, id, data)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Not found.")
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Could not update. Contact the administrator."
        )


@user_router.patch("/{id}")
async def update_user(
    id: int,
    data: UserAccountUpdateModel,
    service: UserAccountService = Depends(ServiceDependency("UserAccountService")),
) -> UserAccountModel:
    try:
        result = await asyncio.to_thread(service.update, id, data)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Not found.")
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Could not update. Contact the administrator."
        )


# Delete
@school_router.delete("/{id}", status_code=204)
async def delete_school(
    id: int, service: SchoolService = Depends(ServiceDependency("SchoolService"))
) -> None:
    try:
        await asyncio.to_thread(service.delete, id)
        return None
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Something went wrong. Not deleted."
        )


@classroom_router.delete("/{id}", status_code=204)
async def delete_classroom(
    id: int, service: ClassroomService = Depends(ServiceDependency("ClassroomService"))
) -> None:
    try:
        await asyncio.to_thread(service.delete, id)
        return None
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Something went wrong. Not deleted."
        )


@user_router.delete("/{id}", status_code=204)
async def delete_user(
    id: int,
    service: UserAccountService = Depends(ServiceDependency("UserAccountService")),
) -> None:
    try:
        await asyncio.to_thread(service.delete, id)
        return None
    except ServiceException:
        raise HTTPException(
            status_code=400, detail="Something went wrong. Not deleted."
        )
