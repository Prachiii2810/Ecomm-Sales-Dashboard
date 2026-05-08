import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt

# Page Config
st.set_page_config(page_title="E-commerce Executive Dashboard", layout="wide")

# Custom CSS for a better look
st.markdown(""" <style> .main { background-color: #f5f7f9; } </style> """, unsafe_allow_html=True)

# 1. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['MonthYear'] = df['Order Date'].dt.to_period('M').astype(str)
    return df

df = load_data()

# 2. Sidebar Filters
st.sidebar.header("Filter Results")
region = st.sidebar.multiselect("Select Region:", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Select Category:", options=df['Category'].unique(), default=df['Category'].unique())

filtered_df = df[df['Region'].isin(region) & df['Category'].isin(category)]

# 3. Header & KPI Metrics
st.title("📊 Superstore Strategy Dashboard")
st.markdown("Real-time sales insights and customer segmentation")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}", f"{((filtered_df['Profit'].sum()/filtered_df['Sales'].sum())*100):.1f}% Margin")
col3.metric("Total Orders", filtered_df['Order ID'].nunique())
col4.metric("Avg Order Value", f"${(filtered_df['Sales'].sum() / filtered_df['Order ID'].nunique()):.2f}")

st.divider()

# 4. Charts Row
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Monthly Sales Trend")
    line_data = filtered_df.groupby('MonthYear')['Sales'].sum().reset_index()
    fig_line = px.line(line_data, x='MonthYear', y='Sales', markers=True, template="plotly_white")
    st.plotly_chart(fig_line, use_container_width=True)

with row1_col2:
    st.subheader("Sales by Sub-Category")
    bar_data = filtered_df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=True).reset_index()
    fig_bar = px.bar(bar_data, x='Sales', y='Sub-Category', orientation='h', color='Sales', color_continuous_scale='Blues')
    st.plotly_chart(fig_bar, use_container_width=True)

# 5. Business Strategy Section (RFM Analysis)
st.subheader("💡 Strategic Insights: RFM Segments")
with st.expander("What is RFM?"):
    st.write("Recency, Frequency, and Monetary analysis helps us identify our best customers.")

# Simplified RFM calculation for the dashboard
snapshot_date = df['Order Date'].max() + dt.timedelta(days=1)
rfm = filtered_df.groupby('Customer Name').agg({
    'Order Date': lambda x: (snapshot_date - x.max()).days,
    'Order ID': 'nunique',
    'Sales': 'sum'
}).rename(columns={'Order Date':'Recency', 'Order ID':'Frequency', 'Sales':'Monetary'})

# Create 3D Scatter for high-level insight
fig_rfm = px.scatter(rfm, x='Recency', y='Monetary', size='Frequency', color='Monetary',
                     hover_name=rfm.index, title="Customer Value Distribution")
st.plotly_chart(fig_rfm, use_container_width=True)

# Display a data table of top customers
st.write("### Top 10 Customers in this Category")
st.dataframe(rfm.sort_values('Monetary', ascending=False).head(10), use_container_width=True)
