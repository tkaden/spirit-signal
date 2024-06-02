import unittest
from unittest.mock import patch, MagicMock
from notify import send_email, notify_users

class TestNotify(unittest.TestCase):

    @patch('smtplib.SMTP_SSL')
    def test_send_email(self, MockSMTP):
        mock_smtp_instance = MockSMTP.return_value
        send_email('Test Subject', 'Test Body', 'test@example.com')
        mock_smtp_instance.login.assert_called_once_with('your_email@example.com', 'your_password')
        mock_smtp_instance.sendmail.assert_called_once()

    @patch('notify.send_email')
    def test_notify_users(self, mock_send_email):
        available_spirits = {
            'test@example.com': ['fortaleza', 'g4']
        }
        notify_users(available_spirits)
        mock_send_email.assert_called_once_with(
            'Available Spirits Notification',
            'The following spirits are available:\nVodka\nWhiskey',
            'test@example.com'
        )

if __name__ == "__main__":
    unittest.main()
