FROM python:3.10

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN useradd -m -u 1000 user

USER user
# Set home to the user's home directory
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH\
    NLTK_DATA=/home/user/app/static/nltk

WORKDIR $HOME/app

RUN pwd
RUN ls -alt

COPY --chown=user . $HOME/app

CMD ["python", "app.py"]