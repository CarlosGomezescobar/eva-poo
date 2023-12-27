python3 -m venv myenv
source myenv/bin/activate
deactivate


pip3 install -r requirements.txt

python3 manage.py startapp core
django-admin startproject eva .