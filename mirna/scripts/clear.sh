#! /usr/bin/bash


echo "Current path is ${PWD}"

echo "Delete virtual environments for Django"
if [ -d ${PWD}/venv ]; then
    rm ${PWD}/venv
fi

echo "Delete index"
if [ -d ${PWD}/references/index ]; then
    rm ${PWD}/references/index/*
fi

echo "Delete db.sqlite3"
if [ -f ${PWD}/emirna_backend/erna/db_local.sqlite3 ]; then
    rm ${PWD}/emirna_backend/erna/db_local.sqlite3
fi
if [ -f ${PWD}/emirna_backend/erna/db_dev.sqlite3 ]; then
    rm ${PWD}/emirna_backend/erna/db_dev.sqlite3
fi
