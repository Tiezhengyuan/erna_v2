#! /usr/bin/bash

echo "### Pull source code of front-end..."
if [ -d $PWD/emirna_frontend ]; then
    cd $PWD/emirna_frontend
    git pull origin main
else
    git clone git@github.com:Tiezhengyuan/emirna_frontend.git
    cd $PWD/emirna_frontend
fi

echo "### Build dist from production:"
yarn install
yarn build

# rollback path
cd ..