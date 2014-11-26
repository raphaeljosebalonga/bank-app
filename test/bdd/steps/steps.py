# bank_app.py
import sys
sys.path.insert(0, '../../..')

from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp

from bank_app import app, BANK
from bank.account import Account

@step(u'Given I create account "([^"]*)" with balance of "([^"]*)"')
def given_i_create_account_group1_with_balance_of_group2(step, account_number, balance):
    a = Account(account_number, balance)
    BANK.add_account(a)

@step(u'And I visit the homepage')
def and_i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)


@step(u'When I enter the account number "([^"]*)"')
def when_i_enter_the_account_number_group1(step, account_number):
    form = world.response.forms['account-form']
    form['account_number'] = account_number
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200)


@step(u'Then I see a balance of "([^"]*)"')
def then_i_see_a_balance_of_group1(step, balance):
    assert_in("Balance: {}".format(balance), world.form_response.text)

@step(u'Given I create the following account:')
def given_i_create_the_following_account(step):
    for row in step.hashes:
        a = Account(row['account_number'], row['balance'])
        BANK.add_account(a)
