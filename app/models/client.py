from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import Integer, String
from database import db



class Client(db.Model):
    __tablename__ = "Client"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    user_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(100), nullable=False)
    zip_code: Mapped[int] = mapped_column(Integer, nullable=False)
    profile_pic: Mapped[str] = mapped_column(String(500))
