import streamlit as st
import random

# Function to generate equation with integer solution
def generate_equation():
    a = random.choice(list(set(range(-10, 11)) - {0}))
    x = random.randint(-10, 10)
    b = random.choice(list(set(range(-20, 21)) - {0}))
    c = a * x + b
    return a, b, c, x

# Initialize session state
if 'equation' not in st.session_state:
    st.session_state.equation = generate_equation()

a, b, c, solution = st.session_state.equation

st.title("🎓 Solve for x")
st.write("Solve the following linear equation:")

# Display equation
st.markdown(f"### `{a}x {'+' if b >= 0 else '-'} {abs(b)} = {c}`")

# Input from user
user_answer = st.number_input("Enter the value of x:", value=0, step=1)

# Check answer
if st.button("Check Answer"):
    if user_answer == solution:
        st.success(f"{random.choice(['🎉', '👏', '🥳'])} Correct! {'Adding' if b <=0 else 'Subtracting'} {abs(b)} {'to' if b <=0 else 'from'} both sides and dividing by {a} gives x = {user_answer}.")
    else:
        st.error(f"❌ Not quite. You should {'add' if b <=0 else 'subtract'} {abs(b)} {'to' if b <=0 else 'from'} both sides and divide by {a}.")

