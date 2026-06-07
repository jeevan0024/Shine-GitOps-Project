#!/bin/bash
# Task 4: Install Datadog Agent on EKS via Helm for monitoring and log collection

helm repo add datadog https://helm.datadoghq.com
helm repo update

helm install datadog-agent datadog/datadog \
  --set datadog.apiKey=$DATADOG_API_KEY \
  --set datadog.logs.enabled=true \
  --set datadog.logs.containerCollectAll=true \
  --set datadog.apm.enabled=true \
  --set datadog.processAgent.enabled=true \
  --namespace default

kubectl get pods -l app=datadog-agent

echo "Datadog agent installed. Check https://app.datadoghq.com for metrics and logs."
