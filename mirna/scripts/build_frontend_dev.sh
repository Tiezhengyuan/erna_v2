#! /usr/bin/bash

echo "### Pull or update source code of front-end..."
repo_name=emirna_frontend
path=${PWD}/${repo_name}
if [ -d $path ]; then
    cd $path
    git pull origin main
else
    git clone git@github.com:Tiezhengyuan/emirna_frontend.git
    cd $path
fi

echo "### Build dist from production:"
yarn install
yarn build

# rollback path
cd $PWD