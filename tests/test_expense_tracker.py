import unittest
from unittest.mock import patch
from src.expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):

    @patch("src.api_client.requests.post")
    def test_add_expense(self, mock_post):
        """Test adding an expense using a mocked API call."""
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "description": "Lunch", "amount": 10.5, "date": "2023-11-01"
        }

        tracker = ExpenseTracker()
        response = tracker.add_expense("Lunch", 10.5, "2023-11-01")

        self.assertEqual(response["description"], "Lunch")
        self.assertEqual(response["amount"], 10.5)
        self.assertEqual(response["date"], "2023-11-01")

    @patch("src.api_client.requests.get")
    def test_view_expenses(self, mock_get):
        """Test retrieving expenses using a mocked API call."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"description": "Lunch", "amount": 10.5, "date": "2023-11-01"},
            {"description": "Coffee", "amount": 3.5, "date": "2023-11-02"}
        ]

        tracker = ExpenseTracker()
        expenses = tracker.view_expenses()

        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0]["description"], "Lunch")
        self.assertEqual(expenses[1]["description"], "Coffee")

    @patch("src.api_client.requests.put")
    def test_update_expense(self, mock_put):
        """Test updating an expense using a mocked API call."""
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = {
            "description": "Dinner", "amount": 15.0, "date": "2023-11-02"
        }

        tracker = ExpenseTracker()
        response = tracker.update_expense(1, "Dinner", 15.0, "2023-11-02")

        self.assertEqual(response["description"], "Dinner")
        self.assertEqual(response["amount"], 15.0)
        self.assertEqual(response["date"], "2023-11-02")

    @patch("src.api_client.requests.delete")
    def test_delete_expense(self, mock_delete):
        """Test deleting an expense using a mocked API call."""
        mock_delete.return_value.status_code = 204  # No content response

        tracker = ExpenseTracker()
        response = tracker.delete_expense(1)

        self.assertTrue(response)

if __name__ == "__main__":
    unittest.main()
