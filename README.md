## Lambda-Git

This project syncs git repos between two different providers. Your users can work with BitBucket (or any git provider) and sync the changes to CodeCommit (or any other git provider). 
This project is run as an AWS Lambda function which you call from a webhook.

When the function is called, it installs git in the lambda environment, clones the source repo, and 
mirrors any changes to the destination repo.

This enables you to use a git provider like BitBucket with good support for things like code 
review discussion in Pull Requests, while still using a git provider like CodeCommit with good 
support for integration into other AWS Products. 

### Set up

Zip up the project like this:

`$ zip lamgit.zip git-2.4.3.tar *.sh *.py`

Upload the zip file to a new Lambda function. Create these environment variables:

   - FROM_USER - Username for source git account
   - FROM_PASS - Password for source git account 
   - FROM_REPO - Domain and path for source repo eg. bitbucket.org/user/project.git
   - TO_USER - Username for destination git account
   - TO_PASS - Password for destination git account 
   - TO_REPO - Domain and path for destination repo eg. git-codecommit.ca-central-1.amazonaws.com/v1/repos/project

The project also supports reading these credentials from AWS Secrets Manager. To use this option, create a secret with the above keys, and provide the following environment variables, as supplied by Secrets Manager:

   - SECRET_NAME
   - SECRET_URL
   - SECRET_REGION

Note that you'll need to add permissions for Secrets Manager to the IAM role your lambda is using.
   
Note that special characters in passwords may need to be URL escaped. eg. instead of `@`, `%40`
   
Note that your AWS CodeCommit username & password is different from your IAM username & password. 
   
Configure the function to be callable via API Gateway, and enter the invocation url into your source repo's webhooks setup.

### Thanks

Thanks to [mhart](https://github.com/mhart) of the [LambCI](https://github.com/lambci/lambci) project for the
git tar ball. It turns out that statically compiling git is a very tricky task.

