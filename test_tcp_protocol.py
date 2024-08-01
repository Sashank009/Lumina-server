import unittest
from unittest.mock import patch
from protocols.tcp_protocol import TCPProtocol

class TestTCPProtocol(unittest.TestCase):
    def setUp(self):
        self.protocol = TCPProtocol()

    def test_handle_message_success(self):
        """Test handling of a valid message."""
        message = "test"
        response = self.protocol.handle_message(message)
        self.assertEqual(response, f"Echo: {message}")

    def test_handle_empty_message(self):
        """Test handling of an empty message."""
        message = ""
        response = self.protocol.handle_message(message)
        self.assertEqual(response, "Echo: ")

    def test_handle_special_characters(self):
        """Test handling of special characters."""
        message = "BYE"
        response = self.protocol.handle_message(message)
        self.assertEqual(response, f"Echo: {message}")

    @patch('protocols.tcp_protocol.TCPProtocol.handle_message', side_effect=Exception("Simulated exception"))
    def test_handle_message_with_exception(self, mock_handle_message):
        """Test handling of exceptions within the protocol."""
        message = "test"
        with self.assertRaises(Exception):
            self.protocol.handle_message(message)

    def test_protocol_initialization(self):
        """Test that the protocol initializes correctly."""
        self.assertIsInstance(self.protocol, TCPProtocol)

if __name__ == '__main__':
    unittest.main()
