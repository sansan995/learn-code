#!/bin/sh

curl http://www.baidu.com
res=$?
if test "$res" != "0";
then
  echo "the curl command faild with: $res"
fi

