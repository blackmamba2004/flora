from sqlalchemy.orm import declared_attr, declarative_mixin


@declarative_mixin
class BaseModel:

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}"
    
    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id!r})>"

    def __str__(self):
        return f"<{self.__class__.__name__}(id={self.id!r})>"
