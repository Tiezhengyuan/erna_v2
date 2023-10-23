# eRNA_v2

eRNA_v2 is upgraded from eRNA which is a tool in Perl with GUI interface (Yuan, T., Huang, X., Dittmar, R.L. et al. eRNA: a graphic user interface-based tool optimized for large data analysis from high-throughput RNA sequencing. BMC Genomics 15, 176 (2014). https://doi.org/10.1186/1471-2164-15-176).

eRNA_v2 is a web applicaton for mRNA-seq data analysis. The app aims at fullfilling RNA-seq data analysis at enterprise level.
- Prcess sequencing data determined by mRNA-seq, miRNA-seq, and scRNA-seq etc.
- Manage raw data. fullfill processing up to thousands raw data.
- Allow multiple tasks. Up to hundreds projects inlcuding thousands tasks could be create managed.
- Network connection. The app can be accessed by team members at Group/Division/Department level.
- Inegrate genome annotations into bioinformatic pipelines.

Design and programming of eRNA_v2.
- Front end is Vue-JavaScript.
- Back end is Django-Python.
- Database is Sqlite/MySQL.
- Bioinformatics pipelins are Python tools.

# Development

## Run eRNA_v2 locally

### run front end (Vue JS) locally

```
cd front_end
yarn serve
```

### run front end (Django) locally

```
cd erna
python manage.py runserver
```

### run bioinformatics pipelines saparately

```
cd erna
python erna_app.py <method> [arguments...]
```


## Unit testing
for example test file is tests/test_project.py
```
 python3 manage.py test tests -k test_project -v 2
```


# References
