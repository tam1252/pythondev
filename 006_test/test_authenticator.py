import pytest
from authenticator import Authenticator

@pytest.fixture
def auth():
    auth = Authenticator()
    yield auth
    auth.reset()
    
def test_register_user_login(auth):
    auth.register("user1", "pass1")
    assert auth.users["user1"] == "pass1"
    
def test_register_existing_user(auth):
    auth.register("user1", "pass1")
    with pytest.raises(ValueError):
        auth.register("user1", "pass1")
        
def login_success(auth):
    auth.register("user1", "pass1")
    result = auth.login("user1", "pass1")
    assert result == "ログイン成功"

def test_login_failure(auth):
    auth.register("user1", "pass1")
    with pytest.raises(ValueError):
        auth.login("user1", "wrongpass")