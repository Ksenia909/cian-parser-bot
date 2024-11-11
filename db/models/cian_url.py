from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, Text, ForeignKey

from db import Base


class CianURL(Base):
    __tablename__ = "cian_url"

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('users.telegram_id', ondelete="CASCADE"),
        primary_key=True
    )
    url: Mapped[str | None] = mapped_column(Text, nullable=True)
    metro: Mapped[str | None] = mapped_column(Text, nullable=True)
    time: Mapped[str | None] = mapped_column(Text, nullable=True)
    rooms: Mapped[str | None] = mapped_column(Text, nullable=True)
    price_min: Mapped[str | None] = mapped_column(Text, nullable=True)
    price_max: Mapped[str | None] = mapped_column(Text, nullable=True)

    user: Mapped['User'] = relationship('User', back_populates='user_url')
