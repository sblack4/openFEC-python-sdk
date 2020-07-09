#!/bin/bash
#
# uses openapi-generate to generate SDK
# see https://openapi-generator.tech/


input_spec="https://api.open.fec.gov/swagger/"

openapi-generator generate \
    --api-package openfec_sdk \
    --config config.json \
    --generator-name python \
    --input-spec "${input_spec}" \
    --minimal-update

mv test/test_* test/unit
mv README.md docs/

git restore README.md

pre-commit run -a

echo ''
echo '!!! WARNING !!!'
echo 'One more step, and its a manual one'
echo 'update configuration.py so that basePath points to https://api.open.fec.gov/v1'
echo ''
