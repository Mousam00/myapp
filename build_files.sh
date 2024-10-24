echo " BUILD START"
python3 -m venv env
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo " BUILD END" 
