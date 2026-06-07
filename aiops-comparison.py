# Task 6: Compare open-source AIOps tools vs traditional monitoring for Kubernetes

tools = {
    "Prometheus":   "Metrics scraping and alerting rules for Kubernetes",
    "Grafana":      "Dashboards and visualization for metrics from Prometheus",
    "Loki":         "Log aggregation (like Datadog logs) - open source",
    "Robusta":      "Kubernetes-native alerts with AI root cause analysis",
    "OpenObserve":  "Open source Datadog alternative - logs, metrics, traces in one UI",
}

traditional = {
    "Log analysis":        "Manual grep and search through log files",
    "Alert noise":         "High - many false alarms, needs manual tuning",
    "Root cause":          "Hours of manual investigation by engineers",
    "Anomaly detection":   "Static thresholds only, misses dynamic issues",
    "MTTR":                "High - slow to detect and resolve",
}

ai_assisted = {
    "Log analysis":        "Automatic pattern detection using Claude AI",
    "Alert noise":         "Low - events are correlated, fewer false alarms",
    "Root cause":          "Minutes - Claude analyzes logs and suggests fix instantly",
    "Anomaly detection":   "ML-based dynamic thresholds, detects unusual patterns",
    "MTTR":                "Significantly reduced - faster detection and resolution",
}

print("=== Open Source AIOps Tools ===")
for tool, desc in tools.items():
    print(f"  {tool:15} : {desc}")

print("\n=== Traditional vs AI-Assisted Monitoring ===")
print(f"{'Feature':<25} {'Traditional':<40} {'AI-Assisted (AIOps)'}")
print("-" * 100)
for feature in traditional:
    print(f"{feature:<25} {traditional[feature]:<40} {ai_assisted[feature]}")

print("\n=== Recommended Open Source Stack ===")
print("  Prometheus + Grafana (metrics) + Loki (logs) + Robusta (K8s AI alerts) + Claude API (analysis)")
