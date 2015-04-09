#!/bin/bash
# ls
# pwd
# echo ".."
# ls -al ../
# echo "../.."
# ls -al ../../
# echo "../../.."
# ls -al ../../../
python --version
# cat /home/travis/virtualenv/python2.7_with_system_site_packages/local/lib/python2.7/site-packages/paver/deps/six.py
# cat /home/travis/virtualenv/python2.7_with_system_site_packages/local/lib/python2.7/site-packages/six.py
pip list
# env

export NO_PREREQ_INSTALL="true"
echo $NO_PREREQ_INSTALL
echo "importing"
# echo "import urllib2" | python 
# echo "import urllib" | python 
echo "imported right"

