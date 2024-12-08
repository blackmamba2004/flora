from app.base.dao import BaseDAO
from app.models.user import User


class UserDAO(BaseDAO):
    model = User
