def lambda_handler(event, context):
    print('*********** The event is: ***************')
    print(event)

    token = event.get('authorizationToken')

    if token == 'abc123':
        effect = 'Allow'
    else:
        effect = 'Deny'

    # Dynamically construct the correct region/method ARN
    method_arn = event['methodArn']
    arn_parts = method_arn.split('/')
    resource_arn = arn_parts[0] + '/' + arn_parts[1] + '/*/*'

    authResponse = {
        "principalId": "abc123",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [{
                "Action": "execute-api:Invoke",
                "Resource": [resource_arn],
                "Effect": effect
            }]
        }
    }

    return authResponse
