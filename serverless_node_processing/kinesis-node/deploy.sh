#!/bin/bash

if [[ -z $2 ]]
then
  stackname=node-kinesis-stack
else
  stackname=$2
fi

rm -rf package.yaml

sam package \
    --template-file template.yaml \
    --s3-bucket "dakobed-serverless-apis" \
    --output-template-file package.yaml


aws cloudformation deploy \
    --template-file package.yaml \
    --stack-name ${stackname} \
    --capabilities CAPABILITY_NAMED_IAM
