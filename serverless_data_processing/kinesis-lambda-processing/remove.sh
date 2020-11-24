#!/bin/bash

if [[ -z $2 ]]
then
  stackname=kinesis-lambda-stack
else
  stackname=$2
fi

if [[ $1 == 'aws' ]]
then
  aws cloudformation delete-stack --stack-name  ${stackname}
elif [[ $1 == 'local' ]]
then
  aws --endpoint-url=http://localhost:4566 cloudformation delete-stack --stack-name ${stackname}
else
    echo "choose either local or aws"
fi

