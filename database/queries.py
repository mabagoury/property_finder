from database import models, schemas
from sqlalchemy.future import select
from sqlalchemy import update, insert, delete


async def get_all_properties(session):
    query = select(models.Property)
    result = await session.execute(query)
    return result.scalars().all()


async def get_property(property_id, session):
    query = select(models.Property).where(models.Property.id == property_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def add_property(property_title, property_description, property_address, property_owner_id, session):
    property = models.Property(title=property_title,
                               description=property_description,
                               address=property_address,
                               owner_id=property_owner_id)
    session.add(property)
    await session.commit()
    return property.id


async def update_property(session, property_id, **kwargs):
    # directly return if there is nothing to update
    # if the dictionary is empty the query will be wrong and an exception is thrown
    if not kwargs:
        return
    query = update(models.Property).where(models.Property.id == property_id).values(**kwargs)
    await session.execute(query)
    await session.commit()


async def delete_property(property_id, session):
    query = delete(models.Property).where(models.Property.id == property_id)
    await session.execute(query)
    await session.commit()
