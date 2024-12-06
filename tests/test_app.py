from http import HTTPStatus

from fast_zero.shcemas import UserPublic


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@email.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@email.com',
    }


def test_read_users(client):
    reponse = client.get('/users')
    assert reponse.status_code == HTTPStatus.OK
    assert reponse.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    reponse = client.get('/users')
    assert reponse.status_code == HTTPStatus.OK
    assert reponse.json() == {'users': [user_schema]}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'teste2',
            'password': '123123',
            'email': 'test@email.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'teste2',
        'email': 'test@email.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted!'}
