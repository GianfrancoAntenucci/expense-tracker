import requests
import os

class APIClient:
    BASE_URL = os.getenv("MOCK_API_URL", "http://localhost:5000/expenses")  # Use localhost for testing

    def add_expense(self, description, amount, date):
        payload = {"description": description, "amount": amount, "date": date}
        response = requests.post(f"{self.BASE_URL}/add", json=payload)
        return response.json() if response.status_code == 201 else None

    def view_expenses(self):
        response = requests.get(f"{self.BASE_URL}/list")
        return response.json() if response.status_code == 200 else []

    def update_expense(self, expense_id, description, amount, date):
        payload = {"description": description, "amount": amount, "date": date}
        response = requests.put(f"{self.BASE_URL}/update/{expense_id}", json=payload)
        return response.json() if response.status_code == 200 else None

    def delete_expense(self, expense_id):
        response = requests.delete(f"{self.BASE_URL}/delete/{expense_id}")
        return response.status_code == 204

