from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,relationship


class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(200))
    is_active: Mapped[bool] = mapped_column(default=True)

    subscriptions: Mapped[list["Subscription"]] = relationship(back_populates="user")


class Asset(Base):
    __tablename__="assets"
    id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[str] = mapped_column(index=True)
    current_price: Mapped[Numeric] = mapped_column(Numeric(precision=18,scale=8))
    last_updated: Mapped[datetime] = mapped_column(DateTime,server_default=func.now(), onupdate=func.now())

    subscriptions: Mapped[list["Subscription"]] = relationship(back_populates="asset")


class Subscription(Base):
    __tablename__='subscriptions'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    asset_id: Mapped[int] = mapped_column(ForeignKey("assets.id", ondelete="CASCADE"))
    target_price: Mapped[Numeric] = mapped_column(Numeric(precision=18,scale=8))
    condition: Mapped[str] = mapped_column()
    is_triggered: Mapped[bool] = mapped_column(default=False)

    user: Mapped["UserDB"] = relationship(back_populates="subscriptions")
    asset: Mapped["Asset"] = relationship(back_populates="subscriptions")
