import re
import pandas as pd
import streamlit as st

# Parse the log file
def parse_log(file_path):
    log_data = {
        "Type": [],
        "Message": [],
    }
    
    with open(file_path, "r") as log_file:
        for line in log_file:
            if "ERROR" in line:
                log_data["Type"].append("Error")
                log_data["Message"].append(line.strip())
            elif "WARNING" in line:
                log_data["Type"].append("Warning")
                log_data["Message"].append(line.strip())
            elif "INFO" in line:
                log_data["Type"].append("Info")
                log_data["Message"].append(line.strip())
    
    return pd.DataFrame(log_data)

# File path
log_file_path = "sample.log"

# Parse the log
log_df = parse_log(log_file_path)

# Streamlit Dashboard
st.title("Log File Metrics Dashboard")
st.write("This dashboard visualizes metrics from the parsed log file.")

# Summary Metrics
st.header("Summary Metrics")
total_errors = log_df[log_df["Type"] == "Error"].shape[0]
total_warnings = log_df[log_df["Type"] == "Warning"].shape[0]
total_info = log_df[log_df["Type"] == "Info"].shape[0]

st.write(f"**Total Errors:** {total_errors}")
st.write(f"**Total Warnings:** {total_warnings}")
st.write(f"**Total Info Messages:** {total_info}")

# Visualization
st.header("Visualizations")
st.bar_chart(log_df["Type"].value_counts())

# Detailed Logs
st.header("Detailed Log Messages")
st.write(log_df)