#! /usr/bin/bash
source .env

# echo "### link source code of front-end..."
# repo_name=$(basename "${SOURCE_CODE_FRONTEND}")
# echo $repo_name
# if [ -d $SOURCE_CODE_FRONTEND ]; then
#     if ! [ -h $PWD/$repo_name ]; then
#         echo "### Create a soft link of front-end source code."
#         ln -s $SOURCE_CODE_FRONTEND $repo_name
#     else
#         echo "The soft link of front-end source code is existing. Skipped"
#     fi
# else
#     echo "Error: ${SOURCE_CODE_FRONTEND} is not existing."
# fi

# # echo "### Build dist from production:"
# cd $repo_name
# yarn install
# yarn build

# # rollback path
# cd ..

build dist
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
if [ -d ${SOURCE_CODE_FRONTEND}/dist ]; then
    cp -r ${SOURCE_CODE_FRONTEND}/dist ${path}/
else
    echo "Error: ${SOURCE_CODE_FRONTEND}/dist is not existing."
fi

cd $PWD
