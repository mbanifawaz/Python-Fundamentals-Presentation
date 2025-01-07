import re

# Step 1: Define the log file path
log_file_path = "sample.log"
summary_file_path = "summary.txt"

def parse_log(file_path):
    errors = []
    warnings = []

    # Step 2: Read the log file
    with open(file_path, 'r') as log_file:
        for line in log_file:
            if "ERROR" in line:
                errors.append(line.strip())
            elif "WARNING" in line:
                warnings.append(line.strip())

    return errors, warnings

def save_summary(errors, warnings, output_path):
    # Step 3: Write the summary report
    with open(output_path, 'w') as summary_file:
        summary_file.write("Log Parsing Summary\n")
        summary_file.write("===================\n\n")
        summary_file.write(f"Total Errors: {len(errors)}\n")
        summary_file.write(f"Total Warnings: {len(warnings)}\n\n")

        summary_file.write("Errors:\n")
        summary_file.write("-------\n")
        for error in errors:
            summary_file.write(error + "\n")

        summary_file.write("\nWarnings:\n")
        summary_file.write("---------\n")
        for warning in warnings:
            summary_file.write(warning + "\n")

def print_summary(errors, warnings):
    # Step 4: Print the summary to the console
    print("\nLog Parsing Summary")
    print("===================")
    print(f"\nTotal Errors: {len(errors)}")
    print(f"Total Warnings: {len(warnings)}\n")

    print("Errors:")
    print("-------")
    for error in errors:
        print(f"- {error}")

    print("\nWarnings:")
    print("---------")
    for warning in warnings:
        print(f"- {warning}")

# Execute the parsing, save the summary, and print it
errors, warnings = parse_log(log_file_path)
save_summary(errors, warnings, summary_file_path)
print_summary(errors, warnings)

print(f"\nLog parsing completed. Summary saved to {summary_file_path}")