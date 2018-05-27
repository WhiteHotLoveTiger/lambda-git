import subprocess as sp
import os

BIT_USER = os.environ['BIT_USER']
BIT_PASS = os.environ['BIT_PASS']
BIT_REPO = os.environ['BIT_REPO']
AWS_USER = os.environ['AWS_USER']
AWS_PASS = os.environ['AWS_PASS']
AWS_REPO = os.environ['AWS_REPO']


def lambda_handler(event, context):
    print(sp.getoutput('bash git-mirror.sh '
                       + ' '.join([BIT_USER, BIT_PASS, BIT_REPO,
                                   AWS_USER, AWS_PASS, AWS_REPO])))

    return
