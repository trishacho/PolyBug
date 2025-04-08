
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
import os

# Assuming the function is in update_module.py
from update_module import update_patient

app = Flask(__name__)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

@patch('update_module.request')
@patch('update_module.sqlitecloud.connect')
@patch('update_module.determine_table_name')
@patch.dict(os.environ, {
    'PASSWORD': 'secure_pass',
    'DATABASE_CONNECTOR': 'fake_connector',
    'ARM_3_NAME': 'arm3_table'
})
def test_update_success(mock_determine_table_name, mock_connect, mock_request):
    mock_request.get_json.return_value = {
        'authorization': {'password': 'secure_pass'},
        'patient': {'id': '123', 'name': 'John', 'arm': 'arm3_table'},
        'to_update': {'age': 45, 'status': 'active'}
    }

    mock_determine_table_name.return_value = 'arm3_table'
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn

    with app.test_request_context():
        response, code = update_patient()

    assert code == 200
    assert response.json['message'] == 'data updated successfully!'
    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()

@patch('update_module.request')
def test_missing_authorization(mock_request):
    mock_request.get_json.return_value = {
        'authorization': None,
        'patient': {'id': '123', 'name': 'John'},
        'to_update': {'age': 45}
    }

    with app.test_request_context():
        response, code = update_patient()
    assert code == 400
    assert response.json['message'] == 'Missing authorization information'

@patch('update_module.request')
@patch.dict(os.environ, {'PASSWORD': 'secure_pass'})
def test_wrong_password(mock_request):
    mock_request.get_json.return_value = {
        'authorization': {'password': 'wrong'},
        'patient': {'id': '123', 'name': 'John'},
        'to_update': {'age': 45}
    }

    with app.test_request_context():
        response, code = update_patient()
    assert code == 405
    assert response.json['message'] == 'Incorrect password given or missing password'

@patch('update_module.request')
@patch.dict(os.environ, {'PASSWORD': 'secure_pass'})
def test_missing_patient(mock_request):
    mock_request.get_json.return_value = {
        'authorization': {'password': 'secure_pass'},
        'patient': None,
        'to_update': {'age': 45}
    }

    with app.test_request_context():
        response, code = update_patient()
    assert code == 400
    assert response.json['message'] == 'Missing patient credentials to update information for'

@patch('update_module.request')
@patch.dict(os.environ, {'PASSWORD': 'secure_pass'})
def test_missing_update_data(mock_request):
    mock_request.get_json.return_value = {
        'authorization': {'password': 'secure_pass'},
        'patient': {'id': '123', 'name': 'John'},
        'to_update': None
    }

    with app.test_request_context():
        response, code = update_patient()
    assert code == 400
    assert response.json['message'] == 'Missing information to update original patient information with'
