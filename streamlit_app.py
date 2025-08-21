import streamlit as st
import os
from snowflake.snowpark import Session
from snowflake.cortex import Root

@st.cache_resource
def create_session():
    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": os.getenv("SNOWFLAKE_ROLE"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA")
    }
    return Session.builder.configs(connection_parameters).create()

session = create_session()
root = Root(session)

query = st.text_input("Ask me something:")

if st.button("Search") and query:
    try:
        # Replace with your Cortex search service name
        search_service = root.search("FOMC_MEETING")
        response = search_service.complete(query)
        st.success("Answer:")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")
