from paver.tasks import task, BuildFailure
from paver.easy import *

@task
def unit_tests():
    sh('nosetests test/unit')

@task
def lettuce_tests():
    sh('lettuce test/bdd')

@task
def run_pylint():
    try:
        sh('pylint --msg-template="{path}:{line}:[{msg_id}\
        	({symbol}), {obj}] {msg}" bank/ > pylint.txt')
    except BuildFailure:
    	pass

@needs('unit_tests', 'lettuce_tests', 'run_pylint')
@task
def default():
    pass