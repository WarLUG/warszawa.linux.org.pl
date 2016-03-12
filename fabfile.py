#!/usr/bin/python
# -*- coding: utf8 -*-

from fabric.api import local, env, abort
from fabric.contrib.console import confirm
from fabric.contrib.project import rsync_project


env.site_location = "/home/misc/warlug/public_html"
env.hosts = ['warlug@duch.mimuw.edu.pl']


def _jekyll(args):
    local('bundle exec jekyll {}'.format(args))


def deploy(settings='staging'):
    if not confirm('Do you really want to deploy?'):
        abort('Aborting!')
    _jekyll('build --future')
    rsync_project(local_dir='_site/', remote_dir=env.site_location,
                  delete=True)


def preview():
    _jekyll('serve --future --watch --drafts --config _config.yml,_config-dev.yml')


def check():
    _jekyll('doctor')


def setup():
    local('bundle install --path vendor/bundle')
