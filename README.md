# conformity-tf-scanner
Terraform template scanner using Conformity API

Conformity template scanner accepts CloudFormation templates, in either YAML or JSON format, and Terraform plan templates only in JSON format. 


## Pre-requisites

- You have a Cloud Conformity API key
- You have an AWS account with GitHub actions configured to assume role. We are not using this role to provision any resources, but required for Terraform plan stage.


## Output

The python script reviews the generated Terraform plan against the conformity api to provide you a categorized output of rules , their risk levels and status.
The script is further configured to fail with an exit code of 1 in case of high or Very_high findings. This can be configured as needed.

```bash

{
  "DNS Compliant S3 Bucket Names": {
    "risk": "LOW",
    "status": "SUCCESS"
  },
  "Enable S3 Block Public Access for S3 Buckets": {
    "risk": "MEDIUM",
    "status": "FAILURE"
  },
  .....
  "Secure Transport": {
    "risk": "MEDIUM",
    "status": "FAILURE"
  },
  "Server Side Encryption": {
    "risk": "HIGH",
    "status": "FAILURE"
  },
  "Tags": {
    "risk": "LOW",
    "status": "FAILURE"
  }
}
{'VERY_HIGH': 10, 'MEDIUM': 3, 'LOW': 7, 'HIGH': 1}

```