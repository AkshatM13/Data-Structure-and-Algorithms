import streamlit as st
from streamlit_lottie import st_lottie
import uuid
from datetime import datetime, timedelta
import json
import os

# Helper function to load Lottie animations
def load_lottie_file(filepath: str):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    else:
        st.warning(f"Animation file not found: {filepath}")
        return None

# Load animations (make sure these JSON files exist in your directory)
register_animation = load_lottie_file("register.json")
transaction_animation = load_lottie_file("transaction.json")
admin_animation = load_lottie_file("admin.json")

# User class for individual operations
class User:
    def __init__(self, name, phone, account_number):
        self.name = name
        self.phone = phone
        self.account_number = account_number
        self.mps_id = str(uuid.uuid4())[:8]  # Generate unique MPS ID
        self.transactions = []  # Store transactions
        self.daily_limit = 20000
        self.transaction_count = 0
        self.is_locked = False
        self.lock_until = None

    def add_transaction(self, amount):
        today = datetime.now().date()
        if self.transactions and self.transactions[-1][1].date() < today:
            self.daily_limit = 20000
            self.transaction_count = 0
            self.is_locked = False

        if self.is_locked and datetime.now() < self.lock_until:
            return False, "User locked until tomorrow."

        if self.transaction_count >= 5 or self.daily_limit - amount < 0:
            self.is_locked = True
            self.lock_until = datetime.now() + timedelta(days=1)
            return False, "Daily limit reached! Try again tomorrow."

        self.transactions.append((amount, datetime.now()))
        self.transaction_count += 1
        self.daily_limit -= amount
        return True, f"Transaction successful! Remaining: ₹{self.daily_limit}"

    def view_last_10_transactions(self):
        return self.transactions[-10:]

# Initialize the MPS system in session state
if "mps_system" not in st.session_state:
    st.session_state.mps_system = []

# Streamlit page configuration
st.set_page_config(page_title="Manipal Payment System", page_icon="💳", layout="wide")

# Display logo or title
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", width=200)
else:
    st.sidebar.title("Manipal Payment System (MPS) 💳")

# Sidebar menu navigation
menu = st.sidebar.radio("Navigate", ["🏠 Home", "📝 Register", "💸 Transaction", "📊 Admin Dashboard"])

# Home Page
if menu == "🏠 Home":
    st.title("Welcome to Manipal Payment System (MPS) 💳")
    if register_animation:
        st_lottie(register_animation, speed=1, height=300)
    st.write("Easily manage payments and transactions with your personal MPS account.")

# Register Page
elif menu == "📝 Register":
    st.title("User Registration")
    if register_animation:
        st_lottie(register_animation, speed=1, height=250)

    name = st.text_input("Enter your Name")
    phone = st.text_input("Enter Phone Number")
    account_number = st.text_input("Enter Bank Account Number")

    if st.button("Register"):
        if name and phone and account_number:
            # Create a new user and store in session state
            user = User(name, phone, account_number)
            st.session_state.mps_system.append(user)
            st.success(f"Successfully Registered! Your MPS ID: {user.mps_id}")
        else:
            st.error("All fields are required!")

# Transaction Page
elif menu == "💸 Transaction":
    st.title("Make a Transaction")
    if transaction_animation:
        st_lottie(transaction_animation, speed=1, height=250)

    mps_id = st.text_input("Enter your MPS ID")
    amount = st.number_input("Enter Transaction Amount", min_value=1)

    if st.button("Submit Transaction"):
        user = next((u for u in st.session_state.mps_system if u.mps_id == mps_id), None)
        if user:
            success, msg = user.add_transaction(amount)
            if success:
                st.success(msg)
            else:
                st.error(msg)
        else:
            st.error("Invalid MPS ID. Please try again.")

# Admin Dashboard
elif menu == "📊 Admin Dashboard":
    st.title("Admin Dashboard - User Details")
    if admin_animation:
        st_lottie(admin_animation, speed=1, height=250)

    users = st.session_state.mps_system
    st.metric("Total Registered Users", len(users))

    if users:
        for user in users:
            st.write(f"**Name:** {user.name} | **Phone:** {user.phone} | **Account:** {user.account_number} | **MPS ID:** {user.mps_id}")
    else:
        st.info("No users registered yet.")
