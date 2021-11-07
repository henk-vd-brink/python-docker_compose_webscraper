from dependency_injector import containers, providers

from app.database import Database

from app.repositories import CarListingRepository, AdvertiserRepository
from app.service import CarListingService, AdvertiserService

class Databases(containers.DeclarativeContainer):
    
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

class Advertisers(containers.DeclarativeContainer):

    config = providers.Configuration()
    databases = providers.DependenciesContainer()

    advertiser_repo = providers.Factory(
        AdvertiserRepository,
        session_factory=databases.db_provider.provided.session
    )

    advertiser_service = providers.Factory(
        AdvertiserService,
        advertiser_repository=advertiser_repo
    )

class Application(containers.DeclarativeContainer):

    config = providers.Configuration()
    databases = providers.Container(Databases, config=config.databases)

    car_listing = providers.Container(CarListings, config=config.car_listings, databases=databases)
    advertiser = providers.Container(Advertisers, config=config.advertisers, databases=databases)