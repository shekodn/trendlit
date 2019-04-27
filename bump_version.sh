#!/usr/bin/env bash
set -e

current_version=$(grep RELEASE?= ./Makefile | sed -e 's/RELEASE?=\(.*\)/\1/g')
next_version=$(echo $current_version | awk -F. '{$NF = $NF + 1;} 1' | sed 's/ /./g')

sed -i -e "s/\(RELEASE?=\).*/\1$next_version/" Makefile
