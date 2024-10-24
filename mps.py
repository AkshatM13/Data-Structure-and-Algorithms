import uuid
from datetime import datetime, timedelta

class User:
    def __init__(self, name, phone, account_number):
        self.name = name
        self.phone = phone
        self.account_number = account_number
        self.mps_id = str(uuid.uuid4())[:8]  # Generate unique MPS ID (first 8 chars of UUID)
        self.transactions = []  # Store user's transactions
        self.daily_limit = 20000
        self.transaction_count = 0
        self.is_locked = False
        self.lock_until = None

    def add_transaction(self, amount):
        today = datetime.now().date()

        # Reset daily limit and transaction count if a new day starts
        if self.transactions and self.transactions[-1][1].date() < today:
            self.daily_limit = 20000
            self.transaction_count = 0
            self.is_locked = False

        if self.is_locked and datetime.now() < self.lock_until:
            print("User is locked for the day. Please try again tomorrow.")
            return False

        if self.transaction_count >= 5 or self.daily_limit - amount < 0:
            self.is_locked = True
            self.lock_until = datetime.now() + timedelta(days=1)
            print(f"Daily limit reached. You are locked for today.")
            return False

        # Process the transaction
        self.transactions.append((amount, datetime.now()))
        self.transaction_count += 1
        self.daily_limit -= amount
        print(f"Transaction successful! Remaining daily limit: {self.daily_limit}")
        return True

    def view_last_10_transactions(self):
        print("\n--- Last 10 Transactions ---")
        for i, (amount, timestamp) in enumerate(self.transactions[-10:], 1):
            print(f"{i}. Amount: {amount}, Date: {timestamp}")

class MPS:
    def __init__(self):
        self.users = []

    def register_user(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        account_number = input("Enter Bank Account Number: ")

        user = User(name, phone, account_number)
        self.users.append(user)
        print(f"User registered successfully! MPS ID: {user.mps_id}")

    def get_user_by_id(self, mps_id):
        for user in self.users:
            if user.mps_id == mps_id:
                return user
        print("User not found.")
        return None

    def process_transaction(self):
        mps_id = input("Enter your MPS ID: ")
        user = self.get_user_by_id(mps_id)
        if user:
            amount = int(input("Enter transaction amount: "))
            user.add_transaction(amount)

    def view_user_transactions(self):
        mps_id = input("Enter your MPS ID: ")
        user = self.get_user_by_id(mps_id)
        if user:
            user.view_last_10_transactions()

    def admin_view_users(self):
        print("\n--- Admin User Details ---")
        print(f"Total Users: {len(self.users)}")
        for user in self.users:
            print(f"Name: {user.name}, Phone: {user.phone}, Account: {user.account_number}, MPS ID: {user.mps_id}")

    def menu(self):
        while True:
            print("\n--- MPS System ---")
            print("1. Register User")
            print("2. Process Transaction")
            print("3. View Last 10 Transactions")
            print("4. Admin: View Users")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.process_transaction()
            elif choice == '3':
                self.view_user_transactions()
            elif choice == '4':
                self.admin_view_users()
            elif choice == '5':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the system
if __name__ == "__main__":
    mps_system = MPS()
    mps_system.menu()
