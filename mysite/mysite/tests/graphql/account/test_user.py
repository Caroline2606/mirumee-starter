from ....account.models import User
import json


def test_user_by_id(db, client_query, my_user):
    user = my_user
    response = client_query(
        """
        query myUser($id: ID!) {
            user(id: $id) {
                email
                id
                password
                first_name
                last_name
            }
        }
        """,
        variables={'id': 1}
    )

    content = json.loads(response.content)

    user_response = content['data']['user']

    assert user_response['id'] == str(user.id)
    assert user_response['email'] == user.email
    assert user_response['first_name'] == str(user.first_name)
    assert user_response['last_name'] == str(user.last_name)