import streamlit as st

st.set_page_config(
    page_title="What is WARN ACT?",
    page_icon="👋",
)

st.write("# WARN ACT California Dashboard")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    ## Worker Adjustment and Retraining Notification (WARN)
    WARN Act - Overview
    WARN protects employees, their families, and communities by requiring employers to give a 60-day notice to the affected 
    employees and both state and local representatives before a plant closing or mass layoff. 
    Advance notice provides employees and their families time to transition and adjust to 
    the potential loss of employment, time to seek alternative jobs and, if necessary, time to obtain 
    skills training or retraining to successfully compete in the job market.

    **👈 Select a page from the sidebar** to see the latest data
    ### Want to learn more?
    - WARN ACT California [Warn ACT](https://edd.ca.gov/en/Jobs_and_Training/Layoff_Services_WARN)
"""
)