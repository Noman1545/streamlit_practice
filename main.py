import streamlit as st

st.title("Chai Maker")
st.write("Apni pasand ki chai tayyar karein.")

tea_type = st.radio("Chai ka base select karein:", ["Milk", "Water"])
flavor = st.selectbox("Flavor select karein:", ["Adrak", "Masala"])
add_masala = st.checkbox("Extra masala add karein")
sugar = st.slider("Sugar level (spoons):", min_value=0, max_value=5, value=2)

if add_masala:
    st.info("Extra masala add kiya jayega.")

st.write(f"Aap ne {tea_type} base aur {flavor} flavor choose kiya hai.")
st.write(f"Sugar: {sugar} spoon")

if st.button("Make Chai"):
    st.success("Aapki chai order ho gayi hai!")
