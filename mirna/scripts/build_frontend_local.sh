#! /usr/bin/bash
source .env

# build dist
if [ -d $SOURCE_CODE_FRONTEND ]; then
    cd $SOURCE_CODE_FRONTEND
    yarn install
    yarn build
else
    echo "Error: ${SOURCE_CODE_FRONTEND} is not existing."
fi

repo_name=$(basename "${SOURCE_CODE_FRONTEND}")
path=${PWD}/${repo_name}
if ! [ -d $path ]; then
    mkdir $path
fi
# copy dist
cp -r ${SOURCE_CODE_FRONTEND}/dist ${path}/

cd $PWD
