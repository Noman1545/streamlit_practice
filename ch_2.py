import streamlit as st

st.title("Chai Maker")
st.write("Apni pasand ki chai tayyar karein.")

customer_name = st.text_input("Apna naam likhein:", placeholder="Example: Noman")
date_of_birth = st.date_input(
    "Apni date of birth select karein:",
    value="2000-01-01",
    min_value="1900-01-01",
    max_value="today",
)
order_date = st.date_input(
    "Order ki date select karein:",
    value="today",
    min_value="today",
)
tea_type = st.radio("Chai ka base select karein:", ["Milk", "Water"])
flavor = st.selectbox("Flavor select karein:", ["Adrak", "Masala"])
add_masala = st.checkbox("Extra masala add karein")
sugar = st.slider("Sugar level (spoons):", min_value=0, max_value=5, value=2)
number_of_cups = st.number_input(
    "Kitne cups chahiye?", min_value=1, max_value=10, value=1, step=1
)

if st.button("Make Chai"):
    if not customer_name.strip():
        st.warning("Order place karne ke liye apna naam likhein.")
    else:
        masala_text = "with extra masala" if add_masala else "without extra masala"
        st.success(f"{customer_name} ki chai order ho gayi hai!")
        st.write(f"Date of birth: {date_of_birth}")
        st.write(f"Date: {order_date}")
        st.write(
            f"{number_of_cups} cup(s) {tea_type} {flavor} chai, "
            f"{sugar} spoon sugar, {masala_text}."
        )
