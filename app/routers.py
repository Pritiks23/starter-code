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
    AssignmentPostModel,
    AssignmentUpdateModel,
    AssignmentModel,
)
from app.services import (
    ClassroomService,
    SchoolService,
    ServiceDependency,
    UserAccountService,
)
from app.db import Assignment, Classroom, UserAccount, SessionLocal

# -----------------------------
# Routers
# -----------------------------
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

assignment_router = APIRouter(
    prefix="/assignment",
    tags=["assignment"],
    responses={404: {"description": "Not Found"}},
)

# -----------------------------
# School Routes
# -----------------------------
@school_router.get("/")
async def list_schools(
    ids: Annotated[Optional[int], Query(alias="schools")] = None,
    service: SchoolService = Depends(ServiceDependency("SchoolService")),
) -> List[SchoolModel]:
    return await asyncio.to_thread(service.get_list, ids)


@school_router.get("/{id}")
async def get_school(
    id: int, service: SchoolService = Depends(ServiceDependency("SchoolService"))
) -> SchoolModel:
    result = await asyncio.to_thread(service.get, id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Not found.")


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

# -----------------------------
# Classroom Routes
# -----------------------------
@classroom_router.get("/")
async def list_classrooms(
    ids: Annotated[Optional[int], Query(alias="classrooms")] = None,
    service: ClassroomService = Depends(ServiceDependency("ClassroomService")),
) -> List[ClassroomModel]:
    return await asyncio.to_thread(service.get_list, ids)


@classroom_router.get("/{id}")
async def get_classroom(
    id: int, service: ClassroomService = Depends(ServiceDependency("ClassroomService"))
) -> ClassroomModel:
    result = await asyncio.to_thread(service.get, id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Not found.")


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

# -----------------------------
# User Routes
# -----------------------------
@user_router.get("/")
async def list_users(
    ids: Annotated[Optional[int], Query(alias="users")] = None,
    service: UserAccountService = Depends(ServiceDependency("UserAccountService")),
) -> List[UserAccountModel]:
    return await asyncio.to_thread(service.get_list, ids)


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

# -----------------------------
# Assignment Routes
# -----------------------------
@assignment_router.get("/", response_model=List[AssignmentModel])
async def list_assignments(
    classroom_name: Optional[str] = None,
    student_name: Optional[str] = None,
):
    def db_task():
        db = SessionLocal()
        try:
            query = db.query(Assignment)
            if classroom_name:
                query = query.join(Classroom).filter(Classroom.name.ilike(f"%{classroom_name}%"))
            if student_name:
                query = query.join(UserAccount).filter(UserAccount.name.ilike(f"%{student_name}%"))
            return query.all()
        finally:
            db.close()
    return await asyncio.to_thread(db_task)


@assignment_router.post("/", response_model=AssignmentModel)
async def create_assignment(data: AssignmentPostModel):
    def db_task():
        db = SessionLocal()
        try:
            classroom = db.query(Classroom).filter(Classroom.id == data.classroom_id).first()
            student = db.query(UserAccount).filter(UserAccount.id == data.student_id).first()
            if not classroom or not student:
                raise ServiceException("Classroom or Student not found")
            assignment = Assignment(
                title=data.title,
                body=data.body,
                submission_date=data.submission_date,
                classroom_id=data.classroom_id,
                student_id=data.student_id,
            )
            db.add(assignment)
            db.commit()
            db.refresh(assignment)
            return assignment
        finally:
            db.close()
    try:
        return await asyncio.to_thread(db_task)
    except ServiceException as e:
        raise HTTPException(status_code=404, detail=str(e))


@assignment_router.get("/{id}", response_model=AssignmentModel)
async def get_assignment(id: int):
    def db_task():
        db = SessionLocal()
        try:
            return db.query(Assignment).filter(Assignment.id == id).first()
        finally:
            db.close()
    assignment = await asyncio.to_thread(db_task)
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignment


@assignment_router.patch("/{id}", response_model=AssignmentModel)
async def update_assignment(id: int, data: AssignmentUpdateModel):
    def db_task():
        db = SessionLocal()
        try:
            assignment = db.query(Assignment).filter(Assignment.id == id).first()
            if not assignment:
                raise ServiceException("Assignment not found")
            for field, value in data.dict(exclude_unset=True).items():
                setattr(assignment, field, value)
            db.commit()
            db.refresh(assignment)
            return assignment
        finally:
            db.close()
    try:
        return await asyncio.to_thread(db_task)
    except ServiceException as e:
        raise HTTPException(status_code=404, detail=str(e))


@assignment_router.delete("/{id}", status_code=204)
async def delete_assignment(id: int):
    def db_task():
        db = SessionLocal()
        try:
            assignment = db.query(Assignment).filter(Assignment.id == id).first()
            if not assignment:
                raise ServiceException("Assignment not found")
            db.delete(assignment)
            db.commit()
        finally:
            db.close()
    try:
        await asyncio.to_thread(db_task)
        return None
    except ServiceException as e:
        raise HTTPException(status_code=404, detail=str(e))

