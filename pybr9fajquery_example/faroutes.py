from pybr9fajquery_example import models
import logging

log = logging.getLogger(__name__)

def includeme(config):
    settings = config.registry.settings.get('pybr9fajquery_example.fa_config', {})

    # Example to add a specific model
    config.formalchemy_model("/my_model",
                             model='pybr9fajquery_example.models.MyModel',
                             **settings)
    # Example to add a specific model
    config.formalchemy_model("/article",
                             model='pybr9fajquery_example.models.Article',
                             **settings)


    log.info('pybr9fajquery_example.faroutes loaded')
