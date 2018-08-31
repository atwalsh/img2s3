from sqlalchemy import func

from img2s3.extensions import db


class BaseModel(db.Model):
    """
    Base model used for all models.
    """
    __abstract__ = True
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.statement_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.statement_timestamp(),
                           onupdate=func.clock_timestamp())
