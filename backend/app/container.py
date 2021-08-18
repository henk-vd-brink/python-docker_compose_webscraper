from dependency_injector import containers, providers

from app.database import Database

from app.repositories.car_listing_repository import CarListingRepository
from app.service import CarListingService




class Databases(containers.DeclarativeContainer):
    """

    Singleton provider provides single object.
    It memorizes the first created object and returns it
    on the rest of the calls.
    """

    config = providers.Configuration()

    db_provider = providers.Singleton(Database, db_url="postgresql://postgres:postgres@database:5432")


class CarListings(containers.DeclarativeContainer):

    config = providers.Configuration()
    databases = providers.DependenciesContainer()

    car_listing_repo = providers.Factory(
        CarListingRepository,
        session_factory=databases.db_provider.provided.session
    )

    car_listing_service = providers.Factory(
        CarListingService,
        car_listing_repository=car_listing_repo
    )

class Application(containers.DeclarativeContainer):

    config = providers.Configuration()

    databases = providers.Container(Databases, config=config.databases)

    car_listing = providers.Container(CarListings, config=config.car_listings, databases=databases)