"""
This script writes two records to Kinesis, triggering the Lambda function

This script takes a single command line argument
if 'local', then makes use of the localstack endpoint.

"""
# !/usr/bin/env python3

import boto3
import json
import time
import sys
import uuid
import datetime


def put_kinesis_records(kinesis_client):
    """
    This function writes several records to a kinesis stream
    :param kinesis_client: kinesis boto3 client
    """
    stream_name = 'OrdersStream'

    payload = {
        'orderID': str(uuid.uuid1()),
        'customerID': 'jerry@gmail.com',
        'products': [{"product_name": "product1", "quantity": 1}, {"product_name": "product2", "quantity": 4}],
        'status': 'CREATING'
    }

    put_response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(payload),
        PartitionKey=str(5))

    print(put_response)


dtime = datetime.datetime.now()

if __name__ == '__main__':
    kinesis_client = boto3.client('kinesis', endpoint_url='http://localhost:4566', region_name='us-west-2') if str(
        sys.argv[1]) == 'local' \
        else boto3.client('kinesis', region_name='us-west-2')

    put_kinesis_records(kinesis_client)
