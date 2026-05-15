def analyze_logs(log_content: str):

    lines = log_content.splitlines()

    summary = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    errors = []
    warnings = []
    timestamps = []

    for line in lines:

        parts = line.split(" ")

        if len(parts) >= 2:
            timestamps.append(f"{parts[0]} {parts[1]}")

        if "INFO" in line:
            summary["INFO"] += 1

        elif "WARNING" in line:
            summary["WARNING"] += 1
            warnings.append(line)

        elif "ERROR" in line:
            summary["ERROR"] += 1
            errors.append(line)

    total_logs = len(lines)

    info_count = summary["INFO"]
    warning_count = summary["WARNING"]
    error_count = summary["ERROR"]

    severity_percentage = {
        "INFO": round((info_count / total_logs) * 100, 2) if total_logs else 0,
        "WARNING": round((warning_count / total_logs) * 100, 2) if total_logs else 0,
        "ERROR": round((error_count / total_logs) * 100, 2) if total_logs else 0
    }

    return {
        "total_logs": total_logs,
        "summary": summary,
        "severity_percentage": severity_percentage,
        "warning_logs": warnings,
        "error_logs": errors,
        "timestamps": timestamps
    }