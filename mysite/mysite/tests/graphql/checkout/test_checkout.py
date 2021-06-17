import json

def test_checkout_by_id(db, client_query, my_checkout ):
    checkout = my_checkout
    response = client_query(
        """
        query mycheckout($id: ID!) {
            checkout(id: $id) {
                id
                lines {
                    id
                    totalPrice
                }
                totalPrice
            }
        }
    }
        """,
        variables={'id': 1}
    )

    content = json.loads(response.content)

    checkout_response = content['data']['checkout']

    assert checkout_response['id'] == str(checkout.id)
    assert checkout_response['user_email'] == str(checkout.user_email)
    assert checkout_response['lines'] == checkout.variant_id, checkout.quantity