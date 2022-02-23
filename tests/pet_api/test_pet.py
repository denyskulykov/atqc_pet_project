import pytest
from faker import Faker
from hamcrest import assert_that, equal_to

from core.client import PetModel, CategoryModel

fake = Faker()

#  move to file Constants
PET_NOT_FOUND = {'code': 1, 'type': 'error', 'message': 'Pet not found'}


@pytest.mark.pet
@pytest.mark.positive
def test_create_pet_with_category(pet_client):
    """Perform testing for pet creation with category

    ID: 101

    Steps: Create Pet

    Expectedresults: Pet should be created with correct fields

    Importance: Critical
    """

    pet = PetModel.create(category=CategoryModel())

    actual_pet = pet_client.create_pet(pet)
    assert_that(actual_pet, equal_to(pet))


@pytest.mark.pet
@pytest.mark.positive
def test_create_pet_without_category(pet_client):
    """Perform testing for pet creation without category

    ID: 102

    Steps: Create Pet

    Expectedresults:
        Pet should be created with correct fields
        Pet should have default Category

    Importance: Critical
    """
    pet = PetModel.create()

    actual_pet = pet_client.create_pet(pet)

    pet.category = CategoryModel(id=0, name=None)
    assert_that(actual_pet, equal_to(pet))


@pytest.mark.pet
@pytest.mark.negative
def test_get_non_existent_pet(pet_client):
    """
    ID: 103

    Steps: Get non existent pet

    Expectedresults:
        Status code should be 404
        Response should have message 'Pet not found'

    Importance: Critical
    """
    response = pet_client.get_pet(
        fake.random.randint(1000, 1000000),
        check_response=False,
        return_raw_response=True
    )
    assert_that(response.status_code, equal_to(404))
    assert_that(response.json(), equal_to(PET_NOT_FOUND))
