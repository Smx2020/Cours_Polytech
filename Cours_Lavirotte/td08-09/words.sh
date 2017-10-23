#!/bin/bash

cat test.txt |tr [:punct:] "\n" |tr [:space:] "\n"|grep "^*"
