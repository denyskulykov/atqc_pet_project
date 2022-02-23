from dataclasses import dataclass, asdict

import json
from faker import Faker
from hamcrest import assert_that, equal_to

from core.base_client import post, get

fake = Faker(['en-US'])

# move to file Endpoints
PET_ENDPOINT = '/v2/pet'


# move to file Model
@dataclass
class CategoryModel:
    id: int = 0
    name: str | None = ''

    @classmethod
    def create(cls, category_id, name):
        return cls(
            id=category_id or fake.random.randint(1, 100),
            name=name or fake.name(),
        )

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, default=lambda x: str(x))

    @classmethod
    def parsing_from_response(cls, resp):
        data = resp.json()
        #  ToDo refactor to marshmallow
        return cls(
            id=data.get('category', {}).get('id'),
            name=data.get('category', {}).get('name'),
        )


@dataclass
class PetModel:
    id: int = 0
    name: str = ''
    status: str = ''
    category: CategoryModel | None = None
    photo_urls: list | None = None  # not implement
    tags: list | None = None  # not implement

    @classmethod
    def create(cls, name='', status='', category=None):
        return cls(
            id=fake.random.randint(1, 10000),
            name=name or fake.name(),
            status=status or 'available',
            category=category or dict(),
            photo_urls=list(),
            tags=list()
        )

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, default=lambda x: str(x))

    @classmethod
    def parsing_from_response(cls, resp):
        data = resp.json()
        #  ToDo refactor to marshmallow
        return cls(
            id=data['id'],
            name=data['name'],
            status=data['status'],
            category=CategoryModel.parsing_from_response(resp),
            photo_urls=data.get('photoUrls', list()),
            tags=data.get('tags', list())
        )


class PetApi:
    """ Class implements client of Pet Api"""

    def __init__(self, host, user, password):
        self.hostname = host  # get from config
        self.cred = (user, password)  # get from config

    def create_pet(self, pet: PetModel, check_response=True, return_raw_response=False):
        resp = post(f'{self.hostname}{PET_ENDPOINT}', json=pet.to_dict(), auth=self.cred)

        if check_response:
            assert_that(resp.status_code, equal_to(200))

        return resp if return_raw_response else PetModel.parsing_from_response(resp)

    def get_pet(self, pet_id: int, check_response=True, return_raw_response=False):
        resp = get(f'{self.hostname}{PET_ENDPOINT}/{pet_id}', auth=self.cred)

        if check_response:
            assert_that(resp.status_code, equal_to(200))

        return resp if return_raw_response else PetModel.parsing_from_response(resp)

    def get_pets_by_status(self):
        pass

    def update_pet(self):
        pass

    def delete_pet(self):
        pass


class UserApi:
    """ Class implements client of User Api"""
    pass


class StoreApi:
    """ Class implements client of Store Api"""
    pass
