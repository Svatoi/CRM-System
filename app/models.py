from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, ForeignKey, DateTime
from datetime import datetime

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), default='user')

    orders: Mapped[list["Order"]] = relationship("Order", back_populates="author", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User {self.username}>"
    
class Order(db.Model):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_name: Mapped[str] = mapped_column(String(100), nullable=False)
    product: Mapped[str] = mapped_column(String(100), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default='New')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    author: Mapped["User"] = relationship("User", back_populates="orders")

    @property
    def total_cost(self):
        return self.quantity * self.price
    
    def __repr__(self):
        return f"<Order {self.id} - {self.product}>"