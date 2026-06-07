#!/bin/bash
# Task 2: Create EKS cluster, namespaces, and RBAC for Shine GitOps Project

eksctl create cluster \
  --name shine-cluster \
  --region ap-south-2 \
  --nodegroup-name shine-nodes \
  --node-type t3.small \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --managed

aws eks update-kubeconfig --name shine-cluster --region ap-south-2

kubectl create namespace retail
kubectl create namespace argocd
kubectl create namespace argo-rollouts

kubectl create serviceaccount retail-sa -n retail

kubectl create clusterrolebinding retail-admin \
  --clusterrole=cluster-admin \
  --serviceaccount=retail:retail-sa

kubectl get nodes
kubectl get ns
