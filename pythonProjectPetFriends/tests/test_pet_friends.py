from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200, f"Expected status code 200, but got {status}"
    assert 'pets' in result, "Response does not contain pet information"
    assert len(result['pets']) > 0, "No pets found"

def test_add_new_pet_with_valid_data(name='Арчи', animal_type='собака', age='2'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200, f"Expected status code 200, but got {status}"
    assert result['name'] == name, f"Expected pet name '{name}', but got '{result['name']}'"


def test_success_ful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, myPets = pf.get_list_of_pets(auth_key, "my_pets")

    if isinstance(myPets, dict) and 'pets' in myPets:
        pets_list = myPets['pets']
        if len(pets_list) > 0:
            pet_id = pets_list[0]['id']
            status, result = pf.delete_pet(auth_key, pet_id)
            assert status == 200
        else:
            print("Нет питомцев для удаления")
    else:
        print("Ошибка при получении списка питомцев")


def test_success_ful_update_self_petInfo():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, myPets = pf.get_list_of_pets(auth_key, "my_pets")

    if isinstance(myPets, dict) and 'pets' in myPets:
        pets_list = myPets['pets']
        if len(pets_list) > 0:
            pet_id = pets_list[0]['id']
            new_name = 'Арчи'
            new_animal_type = 'Собака'
            new_age = 2
            status, result = pf.update_pet_info(auth_key, pet_id, new_name, new_animal_type, new_age)
            assert status == 200
        else:
            print("Нет питомцев для обновления")
    else:
        print("Ошибка при получении списка питомцев")


def test_success_ful_update_self_pet_info(name='Вискас', animal_type='кот', age=1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, myPets = pf.get_list_of_pets(auth_key, "my_pets")

    if isinstance(myPets, dict) and 'pets' in myPets:
        if len(myPets['pets']) > 0:
            status, result = pf.update_pet_info(auth_key, myPets['pets'][0]['id'], name, animal_type, age)
            assert status == 200
            assert result['name'] == name
        else:
            raise Exception("There is no my pets")


