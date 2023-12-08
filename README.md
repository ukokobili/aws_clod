# aws_clod

### creating role for lambda function from AWC CLI
aws iam create-role --role-name lambda-ex --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

### creating a lambda function from AWS CLI
aws lambda create-function –boto-function UpperCaseFunction \
-- zip-file fileb:// boto_function.zip --handler
lambda_function.lambda_handler \
--runtime python3.8 --role <YOUR IAM ARN ROLE>

### creating a lambda function from AWS CLI
aws lambda create-function --function-name upload_function \
--zip-file fileb://my_functions.zip --handler index.handler --runtime python3.9 \
--role arn:aws:iam::633287417316:role/lambda-ex

aws lambda create-function --function-name boto-function \
--zip-file fileb://boto-function.zip --handler lambda_function.lambda_handler --runtime python3.9 \
--role arn:aws:iam::633287417316:role/lambda-ex

### Creating a .zip deployment package with dependencies
To create the deployment package (project directory) ```cd my_project```

Create a new directory named package into which you will install your dependencies. ```mkdir package```

Install your dependencies in the package directory. The example below installs the Boto3 SDK from the Python Package Index using pip. If your function code uses Python packages you have created yourself, save them in the package directory. ```pip install --target ./package boto3 pandas```

Change to the package directory ```cd package``` ```zip -r ../my_deployment_package.zip .```

Add the lambda_function.py file to the root of the .zip file ```cd ..``` ```zip my_deployment_package.zip``` lambda_function.py





