#! /usr/bin/bash

source .env

echo "### Pull or update source code:"
repo_name=emirna_backend
path=${PWD}/${repo_name}
if [ -d $path ]; then
    cd $path
    git pull origin main
else
    git clone git@github.com:Tiezhengyuan/emirna_backend.git
fi
cd $PWD

echo "### Setup virtual ENV:"
export mode=${mode}
if [ -d ${PWD}/venv ]; then
    source venv/bin/activate
else
    virtualenv venv
    source venv/bin/activate
    pip install -r "${path}/requirements.txt"
fi

echo "### Download references and initialize database"
export REFERENCES_DIR=${REFERENCES_DIR}
python3  "${path}/erna/scripts/download_references.py"

# rollback to the previous status
deactivate
