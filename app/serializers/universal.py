from app.base.schemas import BaseSchema

from app.base.models import BaseModel

def transform(
    db_obj: BaseModel, 
    target_schema: BaseSchema
):
    data = {}
    for key in db_obj.__table__.columns.keys():
        if key in target_schema.model_fields:
            value = getattr(db_obj, key)
            data[key] = value

    return target_schema(**data)