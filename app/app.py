from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.db import Base, engine
from app.routers import classroom_router, school_router, user_router
from app.routers.assignment_router import assignment_router  # <-- Added

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(school_router)
app.include_router(classroom_router)
app.include_router(user_router)
app.include_router(assignment_router)  # <-- Added

# Root redirect to docs
@app.get("/")
async def root() -> RedirectResponse:
    """
    Handle calls to root domain.

    Returns:
        RedirectResponse: Redirects to /docs
    """
    return RedirectResponse(url="/docs")
