import logging
from app.ext.db import engine
from . import user, task, annotation, priority, situation, category

logging.getLogger().setLevel('INFO')


# Generate all models
def generate_models():
    logging.info('Creating database models...')
    user.Base.metadata.create_all(bind=engine)
    task.Base.metadata.create_all(bind=engine)
    annotation.Base.metadata.create_all(bind=engine)
    priority.Base.metadata.create_all(bind=engine)
    situation.Base.metadata.create_all(bind=engine)
    category.Base.metadata.create_all(bind=engine)
    logging.info('Database models created')