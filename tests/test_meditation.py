import pytest

def test_meditation(client):
    response = client.get('/meditation/')
    assert b"Meditation index page" == response.data
    
