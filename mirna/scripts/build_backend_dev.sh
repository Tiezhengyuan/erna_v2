#! /usr/bin/bash

source .env

echo "### Pull or update source code:"
if [ -d $PWD/emirna_backend ]; then
    cd $PWD/emirna_backend
    git pull origin main
else
    git clone git@github.com:Tiezhengyuan/emirna_backend.git
    cd $PWD/emirna_backend
fi
    
echo "### Setup virtual ENV:"
if [ -d venv ]; then
    source venv/bin/activate
else
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

# echo "### Migrate database:"
# python3 erna/manage.py makemigrations
# python3 erna/manage.py migrate

# echo "### Create default admin user:"
# export DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
# export DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
# export DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
# python3 erna/manage.py createsuperuser --noinput

echo "### Download references and initialize database"
export mode=${mode}
export RAW_DATA_DIR=${RAW_DATA_DIR}
export REFERENCES_DIR=${REFERENCES_DIR}
# python3 erna/manage.py shell < erna/scripts/init_erna.py
# python3 erna/manage.py shell < erna/scripts/init_raw_data.py
python3 erna/manage.py shell < erna/scripts/init_references.py

# rollback to the previous status
deactivate
cd ..