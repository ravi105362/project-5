import pytest
from src.main import root

def test_hello_world_api():
    output =  root()
    assert output == {"message":"Hello World dev"}