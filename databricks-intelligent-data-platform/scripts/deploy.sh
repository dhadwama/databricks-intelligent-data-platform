#!/bin/bash
# Simple deployment script example

echo "Initializing Terraform"
terraform init

echo "Applying Terraform configuration"
terraform apply -auto-approve

echo "Deployment complete."
