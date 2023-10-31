# encoding: utf-8
"""
Application related tasks for Invoke.
"""

from invoke import Collection

from . import hello, dependencies, db

from config import BaseConfig

namespace = Collection(
    hello,
    dependencies,
    db
)

namespace.configure({
    'app': {
        'static_root': BaseConfig.STATIC_ROOT,
    }
})
