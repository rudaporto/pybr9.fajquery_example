from pybr9fajquery_example import models
import logging

log = logging.getLogger(__name__)


def includeme(config):
    settings = config.registry.settings.get('pybr9fajquery_example.fa_settings}}', {})

    # Example to add a specific model
    #config.formalchemy_model("/my_model", package='pybr9fajquery_example',
    #                         model='pybr9fajquery_example.models.MyModel')
    #                         **settings)

    log.info('pybr9fajquery_example.faroutes loaded')
