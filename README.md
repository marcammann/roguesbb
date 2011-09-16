# Purpose
An SBB Interface, both API and Frontend, based on the inofficial SBB api

# Requirements
* A recent version of Python, including `pip` and `virtualenv`
* hg (Mercurial)

# Installation

```
virtualenv sbb
cd sbb
source bin/activate

git clone git@github.com:marcammann/roguesbb.git

cd roguesbb
pip install -r requirements.txt

python setup.py develop
```

# Start the API Server
```
python sbbapi/manage.py runserver 0.0.0.0:8000    
```

# API Usage Examples
* http://localhost:8000/sbb/1.0/stations.getFromString?station_query=ber
* http://localhost:8000/sbb/1.0/stations.getFromString?station_query=zuri
* http://localhost:8000/sbb/1.0/schedules.query?arrival_id=008503000&departure_id=008503016
* http://localhost:8000/sbb/1.0/schedules.query?arrival_id=008503000&departure_id=008503016&extensive=1

Check `README.API` for more information.


# License 
GPL2

# Disclaimer
"THIS IS A FRIGGIN AWESOME PROJECT!"