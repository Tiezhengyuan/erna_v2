# eRNA_v2

eRNA_v2 is upgraded from eRNA which is a tool in Perl with GUI interface (Yuan, T., Huang, X., Dittmar, R.L. et al. eRNA: a graphic user interface-based tool optimized for large data analysis from high-throughput RNA sequencing. BMC Genomics 15, 176 (2014). https://doi.org/10.1186/1471-2164-15-176).

eRNA_v2 is a web applicaton for mRNA-seq data analysis. The app aims at fullfilling RNA-seq data analysis at enterprise level.
- Prcess sequencing data determined by mRNA-seq, miRNA-seq, and scRNA-seq etc.
- Manage raw data. fullfill processing up to thousands raw data.
- Allow multiple tasks. Up to hundreds projects inlcuding thousands tasks could be create managed.
- Network connection. The app can be accessed by team members at Group/Division/Department level.
- Inegrate genome annotations into bioinformatic pipelines.

Design and programming of eRNA_v2. 
- Front end is Vue2-JavaScript.
- Back end is Django4-Python3.
- Database is Sqlite/MySQL.
- Bioinformatics pipelins are Python3 tools.

# Development

## Run local version of eRNA_v2.
The local version doesn't provide user authentication. And the default databse is sqllite3 rather than MySQL. The app may not be remotely accessed.

### run back end (Django) locally

Django project known as "erna" could be runned locally.
```
cd erna
source venv/bin/activate
pip install -r requiements.txt
python manage.py runserver
```
Once Django server is running:
RestFull APIs are available at http://localhost:8000/api/.
Django Administration is accessible at http://localhost:8000/admin/.

Start Celery in another terminal showed as the below.
It is recommended to test a demo celery task using http://localhost:8000/celery_tasks/test_async/ in broswer. Task ID would reveal asynchronous tasks execution in eRNAv2 is working.
```
cd erna
source venv/bin/activate
celery -A erna worker --beat --scheduler django -l info --pool=solo
```


### run front end (Vue JS) locally

```
cd front_end
yarn serve
```
Access user interface at browser, namely Chrome, at http://localhost:8080/


### run bioinformatics pipelines saparately
All bioinformatics data analysis is taken as asynchronous tasks. A bioinformatics pipeline or even a single step can be executed separately at server.

```
cd erna
python erna_app.py <method> [arguments...]
```


## Unit testing
for example test file is tests/test_project.py
```
 python3 manage.py test tests -k test_project -v 2
```


# Deployment

The app is developed in Linux. Front-end, back-end and data processing are decoupled. It is ok to deploy the three components into different VM depending on the scale of data analysis and complexity of user group.

# References
