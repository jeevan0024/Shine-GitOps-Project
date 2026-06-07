# Task 5: AI-powered Kubernetes troubleshooting agent using Claude AI

import subprocess
import anthropic

# Collect kubectl logs for a pod
def get_logs(pod_name, namespace="retail"):
    result = subprocess.run(
        ["kubectl", "logs", pod_name, "-n", namespace, "--tail=100"],
        capture_output=True, text=True
    )
    return result.stdout

# Collect pod events and status details
def get_events(pod_name, namespace="retail"):
    result = subprocess.run(
        ["kubectl", "describe", "pod", pod_name, "-n", namespace],
        capture_output=True, text=True
    )
    return result.stdout

# Get all pods in namespace
def get_pods(namespace="retail"):
    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", namespace],
        capture_output=True, text=True
    )
    return result.stdout

# Get recent K8s events sorted by time
def get_k8s_events(namespace="retail"):
    result = subprocess.run(
        ["kubectl", "get", "events", "-n", namespace, "--sort-by=.lastTimestamp"],
        capture_output=True, text=True
    )
    return result.stdout

# Send logs and events to Claude for analysis
def analyze_with_claude(logs, events, scenario):
    client = anthropic.Anthropic(api_key="YOUR_CLAUDE_API_KEY")
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": (
                f"Kubernetes issue: {scenario}\n\n"
                f"Pod Logs:\n{logs}\n\n"
                f"Pod Events:\n{events}\n\n"
                "Find the root cause and provide step-by-step remediation."
            )
        }]
    )
    return message.content[0].text

# Scenario 1: Pod continuously restarting (CrashLoopBackOff)
def troubleshoot_pod_restart(pod_name):
    print(f"\n--- Scenario 1: Pod {pod_name} is restarting ---")
    logs = get_logs(pod_name)
    events = get_events(pod_name)
    analysis = analyze_with_claude(logs, events, "pod is continuously restarting / CrashLoopBackOff")
    print(analysis)

# Scenario 2: High latency after deployment
def troubleshoot_high_latency(pod_name):
    print(f"\n--- Scenario 2: High latency detected for {pod_name} ---")
    logs = get_logs(pod_name)
    events = get_events(pod_name)
    analysis = analyze_with_claude(logs, events, "application latency increased after deployment")
    print(analysis)

# Scenario 3: Deployment failed
def troubleshoot_deployment_failure(namespace="retail"):
    print(f"\n--- Scenario 3: Deployment failed in {namespace} ---")
    events = get_k8s_events(namespace)
    pods = get_pods(namespace)
    analysis = analyze_with_claude(pods, events, "deployment failed in Kubernetes")
    print(analysis)

# Main
if __name__ == "__main__":
    pod = "userprofile-rollout-abc123"
    troubleshoot_pod_restart(pod)
    troubleshoot_high_latency(pod)
    troubleshoot_deployment_failure()
