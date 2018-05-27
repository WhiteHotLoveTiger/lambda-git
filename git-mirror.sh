#!/usr/bin/env bash

export GIT_TEMPLATE_DIR='/tmp/usr/share/git-core/templates'
export GIT_EXEC_PATH='/tmp/usr/libexec/git-core'

echo un-taring git...
tar xf git-2.4.3.tar -C /tmp/

echo cloning from bitbucket
cd /tmp/
/tmp/usr/bin/git clone --bare "https://$1:$2@$3"

echo pushing up to aws
cd test-project.git
/tmp/usr/bin/git push --mirror "https://$4:$5@$6"

