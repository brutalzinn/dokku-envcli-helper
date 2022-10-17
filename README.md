# dokku-envcli-helper
Project made to facilitate the import of .env files to Dokku

# Usage

1. Install requirements
> pip install -r requirements.txt

2. Show all commands avaible
> python -m envcli --help

3. Import your local .env file to dokku app named <myname\> 
> python -m envcli generate <myname\> --execute
