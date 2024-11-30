set -o errexit

pip install -r requirements.txt
pip install gunicorn

python manage.py collectstatic --no-input
python manage.py migrate

# Fixing the if statement syntax
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
