import streamlit as st

st.title("streamlit")
st.subheader("frontend practice")
st.text("this is my first frontend code")

gender = st.selectbox(
	"Specify your gender:",
	["male", "female"],
	index=None,
	placeholder="Select your gender",
)

if gender is not None:
	st.write(f"Your gender is {gender}")
	st.success("Selected")