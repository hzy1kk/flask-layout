from app import app


def test_validacao_route_renders_form():
    client = app.test_client()
    response = client.get('/validacao')

    assert response.status_code == 200
    assert b'Nome' in response.data
    assert b'Sobrenome' in response.data
    assert b'Idade' in response.data


def test_validacao_route_validates_vote_and_drive():
    client = app.test_client()
    response = client.post(
        '/validacao',
        data={
            'nome': 'Maria',
            'sobrenome': 'Silva',
            'idade': '18'
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Pode votar: Sim' in response.data
    assert b'Pode dirigir: Sim' in response.data
