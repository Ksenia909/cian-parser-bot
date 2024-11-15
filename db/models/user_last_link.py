from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, Text

from db import Base


class UserLastLink(Base):
    __tablename__ = "user_last_links"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    last_link: Mapped[str | None] = mapped_column(Text, nullable=True)

