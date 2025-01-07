import random
import datetime

# Define log levels, modules, and example messages
LOG_LEVELS = ["INFO", "DEBUG", "WARNING", "ERROR"]
MODULES = [
    "AuthService", "DataProcessor", "APIGateway", "StorageService",
    "NotificationService", "SchedulerService", "MonitoringService",
    "PaymentGateway", "SecurityService", "CacheService", "FileService"
]
MESSAGES = {
    "INFO": [
        "User login successful. UserID: {user_id}, IP: {ip}, SessionPath: /users/{user_id}/sessions/{session_id}",
        "Request received. Endpoint: {endpoint}, Params: {params}, Status: 200, ResponseTime: {time}ms",
        "Scheduled task completed. TaskID: {task_id}, Details: {task_details}",
        "Metrics collected. CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Nodes: {nodes}",
        "Logout successful. UserID: {user_id}, SessionPath: /users/{user_id}/sessions/{session_id}"
    ],
    "DEBUG": [
        "Starting batch processing. BatchID: {batch_id}, SourcePath: {source_path}, TargetPath: {target_path}",
        "Transforming dataset. DatasetID: {dataset_id}, RowsProcessed: {rows_processed}",
        "Cache hit. Key: {key}, CachePath: /cache/{cache_dir}/{key}",
        "Cache write. Key: {key}, Value: {value}, WritePath: /cache/{cache_dir}/{key}",
        "Data aggregation completed. AggregatedRows: {rows}, FilePath: /data/processed/{file_id}"
    ],
    "WARNING": [
        "Disk utilization high. DiskID: {disk_id}, Used: {usage}%, Threshold: 90%, Path: /mnt/{disk_id}",
        "High memory usage detected. Memory: {memory}%, Node: {node_id}, Application: {app_name}",
        "Packet loss detected. NodeID: {node_id}, LossPercentage: {loss}%, Path: /network/{node_id}",
        "Excessive login attempts. IP: {ip}, Attempts: {attempts}, LockFile: /auth/locks/{ip}",
        "Deprecated API usage detected. Endpoint: {endpoint}, UserAgent: {user_agent}"
    ],
    "ERROR": [
        "Disk read failure. DiskID: {disk_id}, Sector: {sector}, FilePath: /mnt/{disk_id}/data/file_{file_id}",
        "Unauthorized login attempt detected. IP: {ip}, UserID: unknown, Endpoint: /auth/login",
        "Payment declined. TransactionID: {transaction_id}, Error: Invalid card number, Path: /payments/errors/{transaction_id}",
        "Service timeout. Endpoint: {endpoint}, Status: 504, RetryPath: /retries/{retry_id}",
        "Disk write failure. DiskID: {disk_id}, Sector: {sector}, FilePath: /mnt/{disk_id}/data/file_{file_id}"
    ]
}

# Helper functions to generate random values
def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_time():
    return random.randint(50, 5000)

def random_id(prefix):
    return f"{prefix}_{random.randint(1000, 9999)}"

def random_percentage():
    return random.randint(1, 100)

def random_loss():
    return round(random.uniform(0.1, 5.0), 2)

def random_sector():
    return random.randint(100, 5000)

def random_path(base):
    return f"/{base}/{random_id('folder')}/{random_id('file')}.log"

# Generate a log entry
def generate_log_entry():
    level = random.choice(LOG_LEVELS)
    module = random.choice(MODULES)
    message_template = random.choice(MESSAGES[level])
    timestamp = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 3600))
    message = message_template.format(
        user_id=random.randint(1000, 9999),
        session_id=random_id("session"),
        ip=random_ip(),
        endpoint=f"/api/{random.choice(['fetch', 'submit', 'query', 'delete'])}",
        params=f"id={random_id('param')}&status={random.choice(['active', 'pending', 'failed'])}",
        time=random_time(),
        task_id=random_id("task"),
        task_details=f"Clean up temp files from path {random_path('temp')}",
        cpu=random_percentage(),
        memory=random_percentage(),
        disk=random_percentage(),
        nodes=random.randint(10, 50),
        batch_id=random_id("batch"),
        source_path=random_path("data/source"),
        target_path=random_path("data/target"),
        dataset_id=random_id("dataset"),
        rows_processed=random.randint(100, 5000),
        key=random_id("key"),
        value=f"{random.randint(1, 100)} entries",
        cache_dir=random_id("cache"),
        rows=random.randint(1000, 10000),
        file_id=random_id("processed"),
        disk_id=random_id("disk"),
        usage=random_percentage(),
        node_id=random_id("node"),
        loss=random_loss(),
        attempts=random.randint(1, 10),
        retry_id=random_id("retry"),
        app_name=f"app_{random.randint(1, 100)}",
        user_agent=random.choice(["Mozilla/5.0", "curl/7.64.1", "PostmanRuntime/7.29.0"]),
        transaction_id=random_id("txn"),
        sector=random_sector()
    )
    return f"{level:<7} {timestamp.strftime('%Y-%m-%d %H:%M:%S')} Module: {module} {message}"

# Generate a log file with a specified number of lines
def generate_log_file(file_name, line_count):
    with open(file_name, "w") as log_file:
        for _ in range(line_count):
            log_entry = generate_log_entry()
            log_file.write(log_entry + "\n")

# Usage example
if __name__ == "__main__":
    log_file_name = "complex_enterprise_log.txt"
    number_of_lines = 1000  # Adjust this value as needed
    generate_log_file(log_file_name, number_of_lines)
    print(f"Generated {number_of_lines} lines of complex log data in '{log_file_name}'")