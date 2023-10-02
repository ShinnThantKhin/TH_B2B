import streamlit as st

st.title('TH Telemedic B2B Calculator')

st.subheader('TH Fees - 10%')

doctor = st.number_input('Doctor Fees',step=1, value=0, format="%d")
agent = st.number_input('Agent Fees', step=1, value=0, format="%d")

btn = st.button('Calculate')

if btn:
    subtotal = doctor+agent
    th_fees = subtotal/10
    alltotal = subtotal + th_fees
    x = alltotal/1.4
    formatted_sub = "{:.0f}".format(subtotal)
    formatted_th = "{:.0f}".format(th_fees)
    formatted_all= "{:.0f}".format(alltotal)
    formatted_x = "{:.0f}".format(x)
    st.success(f'Subtotal Fees : {formatted_sub} kyats')
    st.success(f'TH Fees : {formatted_sub} kyats')
    st.success(f'Total Fees : {formatted_sub} kyats')
    st.text('Onboard Fees')
    st.success(f'Onboard Fees : {formatted_x} kyats')
    
  