#!/usr/bin/env bash

export GIT_TEMPLATE_DIR='/tmp/usr/share/git-core/templates'
export GIT_EXEC_PATH='/tmp/usr/libexec/git-core'

rm -rf /tmp/repo/
mkdir /tmp/repo/

echo cloning from bitbucket
cd /tmp/repo/
/tmp/usr/bin/git clone --bare "https://$1:$2@$3"

echo pushing up to aws
cd test-project.git
/tmp/usr/bin/git push --mirror "https://$4:$5@$6"
