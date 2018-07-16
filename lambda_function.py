import subprocess as sp
import os
import json
import boto3
from botocore.exceptions import ClientError

print(sp.getoutput('bash git-untar.sh'))


def lambda_handler(event, context):
    secrets = get_secrets()
    print(sp.getoutput('bash git-mirror.sh '
                       + ' '.join([secrets['FROM_USER'], secrets['FROM_PASS'],
                                   secrets['FROM_REPO'], secrets['TO_USER'],
                                   secrets['TO_PASS'], secrets['TO_REPO']])))
    return {
        'statusCode': 200
    }


def get_secrets():
    """Grab the git credentials.

    Check in Secrets Manager if we're given a secret name environment variable,
    otherwise look for credentials passed in as environment variables.

    Returns a dictionary of the git credentials.
    """

    if 'SECRET_NAME' in os.environ:
        secret_name = os.environ['SECRET_NAME']
        endpoint_url = os.environ['SECRET_URL']
        region_name = os.environ['SECRET_REGION']
        secrets_str = '{}'

        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name,
            endpoint_url=endpoint_url
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                print("The requested secret " + secret_name + " was not found")
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                print("The request was invalid due to:", e)
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                print("The request had invalid params:", e)
            else:
                print("Some other error:", e)
        else:
            secrets_str = get_secret_value_response['SecretString']

        secrets = json.loads(secrets_str)

    else:
        secrets = {
            'FROM_USER': os.environ['FROM_USER'],
            'FROM_PASS': os.environ['FROM_PASS'],
            'FROM_REPO': os.environ['FROM_REPO'],
            'TO_USER': os.environ['TO_USER'],
            'TO_PASS': os.environ['TO_PASS'],
            'TO_REPO': os.environ['TO_REPO']
        }

    return secrets
