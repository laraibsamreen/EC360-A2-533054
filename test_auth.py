import unittest
import auth_service

class TestRegistration(unittest.TestCase):
    def setUp(self):
        auth_service.users_db.clear()

    def test_register_success(self):
        self.assertTrue(auth_service.register_user("a@b.com", "password123"))

    def test_duplicate_email(self):
        auth_service.register_user("a@b.com", "password123")
        self.assertFalse(auth_service.register_user("a@b.com", "password123"))

    def test_short_password(self):
        with self.assertRaises(ValueError):
            auth_service.register_user("a@b.com", "short")

    def test_verify_email(self):
        auth_service.register_user("a@b.com", "password123")
        self.assertTrue(auth_service.verify_email("a@b.com"))

if __name__ == "__main__":
    unittest.main()