import requests
import streamlit as st

API_URL = st.secrets.get('API_URL', 'http://localhost:8000')

st.title('ISEN Orders Dashboard')

status_filter = st.selectbox('Status', ['', 'NEW', 'SHIPPED', 'COMPLETED'])
platform_filter = st.selectbox('Platform', ['', 'shopee'])

params = {}

orders = requests.get(f"{API_URL}/orders").json()

if status_filter:
    orders = [o for o in orders if o['status'] == status_filter]
if platform_filter:
    orders = [o for o in orders if o['platform'] == platform_filter]

sort_key = st.selectbox('Sort by', ['created_at', 'total_amount'])
orders = sorted(orders, key=lambda x: x[sort_key])

for o in orders:
    st.subheader(f"Order {o['order_id']} - {o['status']}")
    st.write(o)
    details = requests.get(f"{API_URL}/orders/{o['id']}").json()
    st.write(details['items'])
