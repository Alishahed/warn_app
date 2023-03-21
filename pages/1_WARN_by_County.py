import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import plotly.express as px
import pandas as pd

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data(sql_query):

    # Make an API request.
    query_job = client.query(sql_query)

    # Convert as dataframe
    dataframe = (
        query_job
        .result()
        .to_dataframe()
    )

    return dataframe

query = "SELECT * FROM `streamlit-app-379004.warn_act.warn_2022`"
df = get_data(sql_query = query)
df['Effective_Date'] = pd.to_datetime(df['Effective_Date'],format='%Y-%m-%d')
df['Notice_Date'] = pd.to_datetime(df['Notice_Date'],format='%Y-%m-%d')
df = df.drop(['Address','Layoff_Closure','record'],axis=1)
#df_23 = df[df['Notice_Date'] >'2022-12-31']

df_23 = df
df_county = df_23[['County_Parish','No_Of_Employees']]
df_county['No_Of_Employees'] = df_county['No_Of_Employees'].astype('int')

list_county = sorted(df_23["County_Parish"].unique())
df_county_group = df_county.groupby(['County_Parish']).sum().reset_index().sort_values('No_Of_Employees',ascending=False)

with st.sidebar:
    st.title("Warn Act since July 22 (by County)")


fig = px.bar(df_county_group, x='County_Parish', y='No_Of_Employees',title=f"Number of employees affected since 7/1/22 (Total:{df_county_group['No_Of_Employees'].sum()})")
st.plotly_chart(fig)

st.dataframe(df_county_group)