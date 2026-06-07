#!/bin/bash
# Task 3: Install ArgoCD, Argo Rollouts, and deploy Helm chart to EKS

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl create ns retail

kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'

echo "Waiting for ArgoCD to be ready..."
kubectl wait --for=condition=available deployment/argocd-server -n argocd --timeout=120s

argocd admin initial-password -n argocd

kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml

helm install retail-release ./Retail-chart

kubectl get applications -n argocd
kubectl get pods -n retail
kubectl get svc -n retail
