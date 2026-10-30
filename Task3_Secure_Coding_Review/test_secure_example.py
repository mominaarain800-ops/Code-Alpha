import unittest
from secure_example import find_account, normalize_username


class SecureExampleTests(unittest.TestCase):
    def test_valid_known_user(self):
        account = find_account("momina_01")
        self.assertIsNotNone(account)
        self.assertEqual(account.username, "momina_01")

    def test_unknown_valid_user(self):
        self.assertIsNone(find_account("unknown_123"))

    def test_whitespace_is_trimmed(self):
        self.assertEqual(normalize_username("  student_02 "), "student_02")

    def test_invalid_characters_rejected(self):
        with self.assertRaises(ValueError):
            normalize_username("admin' OR '1'='1")

    def test_too_short_rejected(self):
        with self.assertRaises(ValueError):
            normalize_username("ab")

    def test_non_text_rejected(self):
        with self.assertRaises(ValueError):
            normalize_username(None)


if __name__ == "__main__":
    unittest.main()
