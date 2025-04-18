import streamlit as st
import PyPDF2
from docx import Document
from io import BytesIO
import pandas as pd
import time
import json
import os
import requests
from util import *
from profiliing import profile
from rulesgeneration import generate_rules
import time
from dashboard import show_dashboard
from homepage import home_page

# Initialize session state
if 'uploaded_rules' not in st.session_state:
    st.session_state.uploaded_rules = {}
if 'selected_files' not in st.session_state:
    st.session_state.selected_files = []
if 'generated_results' not in st.session_state:
    st.session_state.generated_results = {}
if 'viewing_file' not in st.session_state:
    st.session_state.viewing_file = None
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None

def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "home"
    
    if st.session_state["page"] == "home":
        home_page()
    elif st.session_state["page"] == "dashboard":
        show_dashboard()



if __name__ == "__main__":

    main()
