import re
import random
import streamlit as st # type: ignore

# Main Page Configuration
st.set_page_config(page_title="Password Strength Generator", page_icon="🔑", layout="centered")

# Inject Tailwind CSS for styling
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        .glow { box-shadow: 0 0 10px rgba(72, 187, 120, 0.7); }
        .progress-bar { transition: width 0.5s ease-in-out; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to generate a strong password
def generate_password():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+"
    return "".join(random.sample(chars, 16))  # Generate a 16-character password

# Function to check password strength
def check_password_strength(password):
    feedback = []
    if len(password) < 12:
        feedback.append("❌ At least 12 characters")
    if not re.search(r'[A-Z]', password):
        feedback.append("❌ At least one uppercase letter")
    if not re.search(r'[a-z]', password):
        feedback.append("❌ At least one lowercase letter")
    if not re.search(r'[0-9]', password):
        feedback.append("❌ At least one digit")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("❌ At least one special character")
    return feedback

# Streamlit App
st.markdown(
    """
    <div class="flex flex-col items-center justify-center min-h-screen bg-gradient-to-r from-blue-50 to-purple-50 p-4">
        <div class="bg-white shadow-2xl rounded-lg p-8 w-full max-w-md">
            <h1 class="text-4xl font-bold text-center text-gray-800 mb-4">🔑 Password Strength Generator</h1>
    """,
    unsafe_allow_html=True,
)

# Password Input and Generate Button
password = st.text_input("Enter or generate a password", type="password", placeholder="Your password", help="Minimum 12 characters with uppercase, lowercase, digits, and special characters.")

if st.button("Generate Strong Password 🔄"):
    password = generate_password()

# Check Password Strength
if st.button("Check Strength 🚀"):
    if password:
        feedback = check_password_strength(password)
        if not feedback:
            st.success("✅ Your password is strong and secure! 🎉")
            st.markdown('<div class="progress-bar" style="width: 100%; height: 10px; background-color: green; border-radius: 5px;"></div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Your password needs improvement:")
            for item in feedback:
                st.write(item)
            st.markdown('<div class="progress-bar" style="width: 50%; height: 10px; background-color: orange; border-radius: 5px;"></div>', unsafe_allow_html=True)
    else:
        st.error("Please enter or generate a password.")

# Footer
st.markdown(
    """
    </div>
    <div class="mt-8 text-center text-gray-600">
        Made with ❤️ using Streamlit
    </div>
    </div>
    """,
    unsafe_allow_html=True,
)
