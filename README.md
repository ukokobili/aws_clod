# aws_clod

### creating role for lambda function from AWC CLI
aws iam create-role --role-name lambda-ex --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

### creating a lambda function from AWS CLI
aws lambda create-function --function-name upload_function \
--zip-file fileb://my_functions.zip --handler index.handler --runtime python3.9 \
--role arn:aws:iam::633287417316:role/lambda-ex





