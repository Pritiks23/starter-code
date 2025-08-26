from typing import List
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, Table, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    configure_mappers,
    mapped_column,
    relationship,
    sessionmaker,
)


engine = create_engine("sqlite:///./app.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


classroom_user_account_table = Table(
    "classroom_user_account_table",
    Base.metadata,
    Column(
        "classroom_id", ForeignKey("classroom.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "user_account_id",
        ForeignKey("user_account.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class School(Base):
    __tablename__ = "school"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    classrooms: Mapped[List["Classroom"]] = relationship(back_populates="school")
    user_accounts: Mapped[List["UserAccount"]] = relationship(back_populates="school")


class Classroom(Base):
    __tablename__ = "classroom"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    school_id: Mapped[int] = mapped_column(ForeignKey("school.id", ondelete="CASCADE"))
    school: Mapped["School"] = relationship(back_populates="classrooms")
    user_accounts: Mapped[List["UserAccount"]] = relationship(
        secondary=classroom_user_account_table, back_populates="classrooms"
    )
    assignments: Mapped[List["Assignment"]] = relationship(
        back_populates="classroom", cascade="all, delete"
    )


class UserAccount(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    is_student: Mapped[bool] = mapped_column(default=True)
    school_id: Mapped[int] = mapped_column(
        ForeignKey("school.id", ondelete="SET NULL"), nullable=True
    )
    school: Mapped["School"] = relationship(back_populates="user_accounts")
    classrooms: Mapped[List["Classroom"]] = relationship(
        secondary=classroom_user_account_table, back_populates="user_accounts"
    )
    assignments: Mapped[List["Assignment"]] = relationship(
        back_populates="student", cascade="all, delete"
    )



class Assignment(Base):
    """
    Represents a student assignment in the system
    """

    __tablename__ = "assignment"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    body: Mapped[str] = mapped_column(String)  # simple text field
    submission_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    classroom_id: Mapped[int] = mapped_column(ForeignKey("classroom.id", ondelete="CASCADE"))
    classroom: Mapped["Classroom"] = relationship("Classroom", back_populates="assignments")

    student_id: Mapped[int] = mapped_column(ForeignKey("user_account.id", ondelete="CASCADE"))
    student: Mapped["UserAccount"] = relationship("UserAccount", back_populates="assignments")

# Configure mappers
Base.registry.configure()
configure_mappers()
