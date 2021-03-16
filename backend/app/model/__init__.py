import logging
from app.ext.db import engine
from . import user, task, item

logging.getLogger().setLevel('INFO')


# Generate all models
def generate_models():
    logging.info('Creating database models...')
    user.Base.metadata.create_all(bind=engine)
    task.Base.metadata.create_all(bind=engine)
    item.Base.metadata.create_all(bind=engine)
    logging.info('Database models created')