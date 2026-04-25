from app import app


def test_home_page():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200


def test_generate_qr_code():
    client = app.test_client()
    response = client.post('/generate', json={
        'url': 'https://example.com'
    })

    data = response.get_json()

    assert response.status_code == 200
    assert 'image' in data
    assert data['image'].startswith('data:image/png;base64,')
    assert data['url'] == 'https://example.com'