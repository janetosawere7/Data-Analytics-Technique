# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:59:52 2020

@author: cs

Imports: os, unittest, class datetime of module datetime
Classes:
    TestMyDataBase: subclass of unittest.TestCase 
        Overrides setUp() (creates a database with an employees table) and 
           tearDown() (removes the database and logs the id of the method 
           with the date and time)
        Defines test_aggregate_maount (testing first.aggregate_amount()) and
           test_average_amount (testing first.average_amount())
"""

import os
import first
import unittest
from datetime import datetime

class TestMyDataBase(unittest.TestCase):
    
    """This defines unittests for module first
    
    An instance tests methods first.aggregate_amount() and 
       first.average_amount(). The setup creates database mydatabase.db
       with populated table mytable, and the teardown removes the database
       and logs the method along with the date and time
       with attributes employee (string, employee name) and amount (real)
    
    Subclass of:
	   unittest.TestCase: adds test_aggregate_amount() and test_average_amount(),
	      redefines setUp() amd tearDown().
	
	Attributes: None
    
    Methods:
        setUp(): creates database mydatabase.db with populated table mytable
        tearDown(): remove the database and log the method along with the 
           date and time 
        test_aggregate_amount(): tests first.aggregate_amount()
        test_average_amount(): tests first.average_amount()
    """
    def setUp(self):
        """Create database mydatabase.db with populated table mytable with
        attributes employee (string, employee name) and amount (real)
        """
        first.create_database()

    def tearDown(self):
        """Remove the database and write to log.txt the method id and the 
        datetime 'dd/mm/yyyy hh:mm:ss''"""
        os.remove("mydatabase.db")
    
        n = datetime.now()
        with open('log.txt', 'a') as f:
            f.write("\n{}, ".format(self.id()))
            f.write("{}/{}/{} {}:{}:{}".format(n.month, n.day, n.year, 
                                                 n.hour, n.minute, n.second))

    def test_aggregate_amount(self):
        """Test first.aggregate_amount(), calling it with a list of 3
        employee names, testing what is returned is almost a given value 
        """
        actual = first.aggregate_amount(['Fred', 'Ed', 'Peg'])
        self.assertAlmostEqual(actual, 20.08, places=2)

    def test_average_amount(self):
        """test first.aggregate_amount(), that what it returns is almost a 
        given value
        """
        actual = first.average_amount()
        self.assertAlmostEqual(actual, 5.59, places=2)
