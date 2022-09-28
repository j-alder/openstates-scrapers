FROM python:3.9-slim
LABEL maintainer="James Turk <dev@jamesturk.net>"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONIOENCODING='utf-8'
ENV LANG='C.UTF-8'

RUN apt-get update -qq \
    && apt-get install -y -qq --no-install-recommends \
      ca-certificates \
      curl \
      wget \
      unzip \
      mdbtools \
      libpq5 \
      libgdal28 \
      build-essential \
      git \
      libssl-dev \
      libffi-dev \
      freetds-dev \
      libxml2-dev \
      libxslt-dev \
      libyaml-dev \
      poppler-utils \
      libpq-dev \
      libgdal-dev \
      libgeos-dev \
      gnupg \
      sudo \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && sudo apt update \
    && sudo apt install gh -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD poetry.lock /opt/openstates/openstates/
ADD pyproject.toml /opt/openstates/openstates/
WORKDIR /opt/openstates/openstates/
ENV PYTHONPATH=./scrapers

RUN pip --no-cache-dir --disable-pip-version-check install poetry \
    && poetry install --no-root \
    && apt-get remove -y -qq \
      build-essential \
      libpq-dev \
    && apt-get autoremove -y -qq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD . /opt/openstates/openstates/
# the last step cleans out temporarily downloaded artifacts for poetry, shrinking our build
RUN poetry install \
    && rm -r /root/.cache/pypoetry/cache /root/.cache/pypoetry/artifacts/

ENV OPENSSL_CONF=/opt/openstates/openstates/openssl.cnf

ENTRYPOINT ["poetry", "run", "os-update"]
