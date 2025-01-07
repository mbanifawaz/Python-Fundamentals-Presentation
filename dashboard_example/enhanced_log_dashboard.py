import re
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Parse the log file
def parse_log(file_path):
    log_data = {
        "Type": [],
        "Message": [],
    }
    
    with open(file_path, "r") as log_file:
        for line in log_file:
            if "ERROR" in line:
                log_data["Type"].append("ERROR")
                log_data["Message"].append(line.strip())
            elif "WARNING" in line:
                log_data["Type"].append("WARNING")
                log_data["Message"].append(line.strip())
            elif "INFO" in line:
                log_data["Type"].append("INFO")
                log_data["Message"].append(line.strip())
            elif "DEBUG" in line:
                log_data["Type"].append("DEBUG")
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
log_summary = log_df["Type"].value_counts()
total_logs = log_summary.sum()

st.write(f"**Total Log Messages:** {total_logs}")
st.write(f"**Total Errors:** {log_summary.get('ERROR', 0)}")
st.write(f"**Total Warnings:** {log_summary.get('WARNING', 0)}")
st.write(f"**Total Info Messages:** {log_summary.get('INFO', 0)}")
st.write(f"**Total Debug Messages:** {log_summary.get('DEBUG', 0)}")

# Visualization: Bar Chart
st.header("Visualizations")
st.subheader("Bar Chart")
st.bar_chart(log_summary)

# Visualization: Pie Chart
st.subheader("Pie Chart")
fig, ax = plt.subplots()
log_summary.plot.pie(
    autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'], ax=ax
)
ax.set_ylabel('')
ax.set_title("Log Message Distribution")
st.pyplot(fig)

# Filtering Logs
st.header("Detailed Log Messages")
filter_type = st.selectbox("Filter by Log Type", options=["All", "ERROR", "WARNING", "INFO", "DEBUG"])
if filter_type != "All":
    filtered_logs = log_df[log_df["Type"] == filter_type]
else:
    filtered_logs = log_df

# Display Logs
st.dataframe(filtered_logs.sort_values(by="Type", ascending=True))
