## Lambda-Git

This project can be run as an AWS Lambda function which you call from a BitBucket Web Hook.
When the function is called, it installs git on the lambda, clones the BitBucket repo, and 
mirrors any changes to an AWS CodeCommit repo.

This enables you to use a git provider like BitBucket with good support for things like code 
review discussion in Pull Requests, while still using a git provider like CodeCommit with good 
support for integration into other AWS Products. 

Note that this project could work for any two git providers, BitBucket & CodeCommit are
just examples.

### Set up

Zip up the project like this:

`$ zip lamgit.zip git-2.4.3.tar git-mirror.sh lambda_function.py`

Upload the zip file to a new Lambda function, and create and fill in these environment variables:

   - BIT_USER - Username for BitBucket Account
   - BIT_PASS - Password for BitBucket Account 
   - BIT_REPO - Domain and path to BitBucket repo
   - AWS_USER - Username for CodeCommit Account
   - AWS_PASS - Password for CodeCommit Account 
   - AWS_REPO - Domain and path to CodeCommit repo
   
   Note that special characters in passwords may need to be URL escaped. eg. instead of `@`, `%40`
   
   Note that your AWS CodeCommit username & password is different from your IAM username & password. 
   
Configure the function to be callable via API Gateway, and enter the invocation url into your BitBucket Web Hooks setup.

### Thanks

Thanks to [mhart](https://github.com/mhart) of the [LambCI](https://github.com/lambci/lambci) project for the
git tar ball. It turns out that statically compiling git is a very tricky task.

