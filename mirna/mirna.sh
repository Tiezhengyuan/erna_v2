#! /usr/bin/bash
# Test, and deploy eRNAv2-mirna

if [ "$1" = build ]; then
    echo "### Pull source code, download references and build database..."
    # test local deployment
    if [ "$2" = local ]; then
        bash scripts/build_frontend_local.sh || true
        bash scripts/build_backend_local.sh || true
    # local deployment
    elif [ "$2" = dev ]; then
        # bash scripts/build_frontend_dev.sh || true
        bash scripts/build_backend_dev.sh || true
    fi

elif [ "$1" = start ]; then
    echo "### Build images and start containers..."
    docker-compose up -d
elif [ "$1" = stop ]; then
    echo "### Stop and remove containers..."
    docker-compose down
elif [ "$1" = clear ];then
    echo "### delete database, app image, and containers..."
    rm emirna_backend/erna/db.sqlite3
    docker rmi mirna-app
    docker rm emirna_backend
    docker rm emirna_frontend
else
    echo $@
    echo "Usage: ./mirna.sh <action> <deployment-mode>"
    echo "action: build|start|stop|clear"
    echo "deployment-mode: local|dev"
fi

echo "current path: ${PWD}"