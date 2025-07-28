# SPDX-FileCopyrightText: 2025 Laurent Prosperi <laurent.prosperi@ens-paris-saclay.fr>
#
# SPDX-License-Identifier: EUPL-1.2

{ config, ... }:

{
  services.django-apps.sites.kadenios = {
    source = "https://git.github.com/severus21/p-jdl";
    branch = "main";
    domain = "https://jdl.laurentprosperi.info/";

    nginx = {
      enableACME = true;
      forceSSL = true;
    };

    dependencies = ps: [
      ps.django
      ps.gunicorn
      ps.networkx
      ps.numpy
      ps.pandas
      ps.matplotlib
      ps.unidecode
      ps.django-crispy-forms
      ps.django-crispy-bootstrap4
    ];

    environment = {
        DJANGO_DEBUG_MODE = false;
    };

    credentials = {
        DJANGO_SECRET_KEY = config.age.secrets."dj_jdl_secret-key".path;
    };
  };
}
