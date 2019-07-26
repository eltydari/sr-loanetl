# -- FILE: environment.py
'''
This file controls the behavior of the behave module
'''
import tempfile as tmp

def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")
        return

def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return
    context.dir = tmp.TemporaryDirectory()

def after_scenario(context, scenario):
    context.dir.cleanup()