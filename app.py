 #  Password Checker 

import streamlit as st
import random
import string

# Page configuration
st.set_page_config(
    page_title="Password Manager",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton {display: flex; justify-content: center;}
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px; padding: 10px;}
    .stButton button:hover {background-color: #45a049;}
   
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔒 Password Manager")
st.write("Store your passwords securely, check their strength, and generate new passwords!")

# Sidebar for password history
st.sidebar.title("📜 Password History")
if 'password_history' not in st.session_state:
    st.session_state.password_history = []

# Function to check password strength
def check_password_strength(password):
    has_numeric = any(char.isdigit() for char in password)  # Check for numeric characters
    has_special = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in password)  # Check for special characters

    if has_numeric and has_special:
        return "✅ **Strong Password** - Your password is secure (contains numbers and special characters)."
    elif has_numeric:
        return "⚠️ **Moderate Password** - Add special characters (e.g., @#$%) to make it stronger."
    elif has_special:
        return "⚠️ **Moderate Password** - Add numbers (0-9) to make it stronger."
    else:
        return "❌ **Weak Password** - Add numbers (0-9) and special characters (e.g., @#$%) to make it stronger."

# Function to generate a random password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))  # Fixed length of 12
    return password

# User input for saving a password
user_password = st.text_input("Enter a password to save:", type="password", help="Type your password here to save it.")

# Buttons for checking strength and saving password
col1, col2 = st.columns(2)
with col1:
    if st.button("Check Strength"):
        if user_password:
            strength_message = check_password_strength(user_password)
            st.markdown(strength_message)
        else:
            st.warning("⚠️ Please enter a password first!")
with col2:
    if st.button("Save Password"):
        if user_password:
            st.session_state.password_history.append(user_password)
            st.success("✅ Password saved successfully!")
        else:
            st.warning("⚠️ Please enter a password first!")

# Display password history in the sidebar
if st.session_state.password_history:
    st.sidebar.write("Saved Passwords:")
    for idx, pwd in enumerate(st.session_state.password_history[::-1], 1):
        st.sidebar.code(f"{idx}. {pwd}", language="text")
else:
    st.sidebar.write("No passwords saved yet.")

# New Password Generator
st.markdown("---")
st.subheader("🔑 Generate a New Password")
if st.button("Generate New Password"):
    new_password = generate_password()
    st.code(f"Generated Password: {new_password}", language="text")
    st.session_state.password_history.append(new_password)
    st.success("✅ New password generated and saved!")


# Footer
st.markdown("---")
st.markdown('<div class="footer">Made with ❤️ by <b> ©Azeezullah Noohpoto </b></div>', unsafe_allow_html=True)