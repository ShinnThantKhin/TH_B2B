import streamlit as st

st.title('TH Telemedic B2B Calculator')

st.subheader('TH Fees - 10%')

doctor_text = st.text_input('Doctor Fees')
agent_text = st.text_input('Agent Fees')

btn = st.button('Calculate')

if btn:
    try:
        doctor = int(doctor_text)
        agent = int(agent_text)
    except ValueError:
        st.warning("Please enter valid integer values for Doctor Fees and Agent Fees.")
    subtotal = doctor+agent
    th_fees = subtotal/10
    alltotal = subtotal + th_fees
    x = alltotal/1.4
    formatted_sub = "{:.0f}".format(subtotal)
    formatted_th = "{:.0f}".format(th_fees)
    formatted_all= "{:.0f}".format(alltotal)
    st.success(f'Subtotal Fees : {formatted_sub} kyats')
    st.success(f'TH Fees : {formatted_th} kyats')
    st.success(f'Total Fees : {formatted_all} kyats')
    st.text('Onboard Fees')
    st.success(f'Onboard Fees : {x} kyats')
    
  
