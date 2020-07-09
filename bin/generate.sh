#!/bin/bash
#
# uses openapi-generate to generate SDK
# see https://openapi-generator.tech/


input_spec="https://api.open.fec.gov/swagger/"

openapi-generator generate \
    --api-package openfec_sdk \
    --config config.json \
    --generator-name python-experimental \
    --input-spec "${input_spec}"

mv test/test_* test/unit
mv README.md docs/

git restore README.md

echo 'update configuration.py so that basePath points to https://api.open.fec.gov/v1'

pre-commit run -a
