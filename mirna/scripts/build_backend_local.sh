#! /usr/bin/bash

source .env

if ! [ -d $SOURCE_CODE_BACKEND ]; then
    echo "Error: ${SOURCE_CODE_BACKEND} is not existing."
fi

repo_name=$(basename "${SOURCE_CODE_BACKEND}")
path=${PWD}/${repo_name}

echo "### Copy/update source code of back-end"
rsync -r --exclude 'venv' --exclude 'results/P*' \
    --exclude 'raw_data/*' --exclude 'logs/*' \
    $SOURCE_CODE_BACKEND ./

echo "### Setup virtual ENV:"
export mode=${mode}
if [ -d venv ]; then
    source venv/bin/activate
else
    virtualenv venv
    source venv/bin/activate
    pip install -r "${path}/requirements.txt"
fi

echo "### Download omics data."
export REFERENCES_DIR=${REFERENCES_DIR}
echo "### current references path: ${REFERENCES_DIR}"
python3 "${path}/erna/scripts/download_references.py"

# rollback to the previous status
deactivate
