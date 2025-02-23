# Expense Tracker (Python CLI with Mocked API)

## 📌 Project Overview
The **Expense Tracker** is a command-line application that allows users to add, view, update, and delete expenses while following **Test-Driven Development (TDD)** principles. It interacts with a **mocked API** using `unittest.mock` to simulate API responses, ensuring isolated and reliable testing.

## 🛠 Features
- 📌 **Add Expenses**: Enter a description, amount, and date.
- 📌 **View Expenses**: Retrieve a list of expenses.
- 📌 **Update Expenses**: Modify an existing expense.
- 📌 **Delete Expenses**: Remove an expense from the list.
- 📌 **Mocked API Calls**: All API interactions are simulated during testing.

## 📂 Project Structure
```
expense_tracker/
│── src/
│   │── __init__.py         # Package identifier
│   │── expense_tracker.py  # Expense Tracker logic & CLI
│   │── api_client.py       # API Client handling API interactions
│── tests/
│   │── test_expense_tracker.py  # Unit tests using mocking
│── cli.py                 # CLI entry point (optional)
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🖥️ Running the CLI
To use the CLI, run:
```bash
python src/expense_tracker.py <command> [arguments]
```

### Available Commands:
- **Add an Expense:**
  ```bash
  python src/expense_tracker.py add "Lunch" 10.5 "2023-11-01"
  ```
- **View Expenses:**
  ```bash
  python src/expense_tracker.py view
  ```
- **Update an Expense:**
  ```bash
  python src/expense_tracker.py update 1 "Dinner" 15.0 "2023-11-02"
  ```
- **Delete an Expense:**
  ```bash
  python src/expense_tracker.py delete 1
  ```

## 🧪 Running Tests (TDD Approach)
The project follows **Test-Driven Development (TDD)**. Run tests with:
```bash
pytest tests/
```
or
```bash
python -m unittest discover tests/
```

## 🔧 Configuration
- The API base URL is set in `api_client.py`.
- You can override it using an environment variable:
  ```bash
  export EXPENSE_TRACKER_API_URL="https://your-api-url.com"
  ```

## 📌 Future Improvements
- ✅ Store expenses in a local database (SQLite or PostgreSQL)
- ✅ Add a graphical user interface (GUI)
- ✅ Implement user authentication

## 📜 License
This project is licensed under the MIT License.

## 👥 Author
**Gianfranco** - [GitHub Profile](https://github.com/GianfrancoAntenucci)

---
Enjoy tracking your expenses efficiently!

