def analyze_logs(log_content: str):

    lines = log_content.splitlines()

    summary = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    errors = []
    warnings = []

    for line in lines:

        if "INFO" in line:
            summary["INFO"] += 1

        elif "WARNING" in line:
            summary["WARNING"] += 1
            warnings.append(line)

        elif "ERROR" in line:
            summary["ERROR"] += 1
            errors.append(line)

    total_logs = len(lines)

    return {
        "total_logs": total_logs,
        "summary": summary,
        "warning_logs": warnings,
        "error_logs": errors
    }