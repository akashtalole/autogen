import pytest
from unittest.mock import MagicMock
from autogen.agentchat.contrib.stream_handler import SimpleClientSocketIOStreamHandler

class TestSimpleClientSocketIOStreamHandler:
    @pytest.fixture
    def mock_socket_client(self):
        return MagicMock()

    @pytest.fixture
    def handler(self, mock_socket_client):
        return SimpleClientSocketIOStreamHandler(mock_socket_client)

    def test_open(self, handler, mock_socket_client):
        url = "http://example.com"
        handler.open(url)
        mock_socket_client.connect.assert_called_once_with(url, None, None, None, '/', 'socket.io', 5)

    def test_write(self, handler, mock_socket_client):
        event = "test_event"
        data = "test_data"
        handler.write(event, data)
        mock_socket_client.emit.assert_called_once_with(event, data)

    def test_close(self, handler, mock_socket_client):
        handler.close()
        mock_socket_client.disconnect.assert_called_once()
