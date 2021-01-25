
"""
This script reads the csv files written by the script scrape_rei_products.py and inserts the products into the Products
dynamoDB table.
"""
# !/usr/bin/env python3

import csv
import os
import boto3
from boto3.dynamodb.types import Decimal
from time import sleep



def create_seaside_table():
    try:
        dynamodb.create_table(
            AttributeDefinitions=[
                {
                    "AttributeName": "category",
                    "AttributeType": "S"
                }
            ],
            TableName='SeaSideTest',
            KeySchema=[
                {
                    "AttributeName": "category",
                    "KeyType": "HASH"
                },

            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            },
        )

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:4566")
    dynamodb = boto3.resource('dynamodb')
    create_seaside_table()
