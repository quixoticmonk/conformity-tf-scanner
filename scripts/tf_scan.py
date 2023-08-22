"""Script to scan your Terraform or Cloudformation template against Conformity API"""
import sys
import json
import requests


import click


@click.command()
@click.option("--region", default="us-1", help="Conformity region")
@click.option("--api_key", help="Conformity API key region")
@click.option("--template_type", default="terraform-template", help="Conformity scanner template type")
@click.option("--template_path", help="Path to the template")
def initiate_scan(region, api_key, template_type, template_path):
    """
    :param region: Cloud conformity region
    :param api_key: API key used to connect with Cloud Conformity
    :param template_type: supported IAC template types : cloudformation-template/terraform-template
    :param template_path: path to the generated template
    """
    conformity_url = f"https://conformity.{region}.cloudone.trendmicro.com/api/template-scanner/scan"

    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': 'ApiKey ' + api_key
    }

    with open(template_path, "r") as template_file:
        payload = {
            'data': {
                'attributes': {
                    'type': template_type,
                    'contents': template_file.read()
                }
            }
        }
        resp = requests.post(conformity_url, headers=headers, data=json.dumps(payload), timeout=20)

    response_object = resp.json()
    scan_status = {}
    scan_summary = {}
    for items in response_object["data"]:
        scan_status[items["attributes"]["rule-title"]] = {
            "status": items["attributes"]["status"],
            "risk": items["attributes"]["risk-level"]
        }
        risk = items["attributes"]["risk-level"]
        if risk in scan_summary:
            scan_summary[items["attributes"]["risk-level"]] += 1
        else:
            scan_summary[items["attributes"]["risk-level"]] = 1

    print(json.dumps(scan_status, indent=2, sort_keys=True))
    print(scan_summary)
    if scan_summary["VERY_HIGH"] + scan_summary["VERY_HIGH"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    initiate_scan()
