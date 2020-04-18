# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:17:12 2020

@author: cs

Imports: sqlite3
"""

import  sqlite3

def create_database():
    """Create database with table mytable and populate from file
    
    Connect to database mydatabase.db, create table mytable (if it doesn't 
    exist) with columns employee (string, a name) and amount(real), and 
    this table with data from file results.txt.
    
    Args: None
    Returns: None
    
    Input:
        File results.txt, each line with an employee's name and amount
    
    Persistent:
        Create in database mydatabase.db table mytable with columns
           employee (string, name) and amount, populated from results.txt
    
    """
    
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    
    sql_command = """
    CREATE TABLE IF NOT EXISTS mytable (
    employee TEXT,
    amount REAL);"""
    cursor.execute(sql_command)
    
    sql_command = """
    INSERT INTO mytable(employee, amount) 
    VALUES (?, ?);"""
    
    with open('results.txt', 'r') as f:
        for line in f:
            
            # The line just read is a string terminated with a newline 
            # containing the employee name and the string version of the 
            # amount, separated by a comma. Extract a list with just
            # the name and the amount string. 
            
            emp, amt = line.replace('\n', '').split(',')
            
            cursor.execute(sql_command, (emp, float(amt)))
    
    connection.commit()
    connection.close

def aggregate_amount(emps):
    """Return sum of the amounts in table employee for those in list emps
    
    Connext to database mydatabase.db and sum all the amount values 
    associated with the employee fields whose values are in the list
    argument emps. Return this sum.
    
    Args:
        emps (list of strings): values that are intended to be values in 
           employee column
    
    Returns:
        Sum of the amount values associated with the employee names in emps
    
    Accesses:
        Database mydatabae.db, with columns employee (string, an employee's
           name) and amount (real))
    """
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    
    sql_command = """
    SELECT amount 
    FROM mytable
    WHERE employee = ?;"""
    result = 0.0
    for e in emps:
        cursor.execute(sql_command, (e,))
        result += cursor.fetchone()[0]
    
    cursor.close()
    connection.close()

    return result

def average_amount():
    """Return average of the values in the amount column of table mytable
    
    Connect to database mydatabase.db and compute and return the average of
    the values in amount column of table mytable in this database
    
    Args: None
    
    Returns:
        Average of the values in the amount column of table mytable in
           databas mydatabase.db
    
    Accesses:
        Database mydatabae.db, with columns employee (string, an employee's
           name) and amount (real))
    """
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    sql_command = """
    SELECT amount
    FROM mytable;"""
    cursor.execute(sql_command)
    result = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return sum([x[0] for x in result]) / len(result)

# =============================================================================
# sql_command = """
# SELECT * FROM mytable;"""
# 
# for row in cursor.execute(sql_command):
#     print(row)
# 
# connection.close()
# =============================================================================

if __name__ == '__main__':
    import os;
    #os.remove("mydatabase.db")
    if not os.path.exists("mydatabase.db"):
        create_database()
    
    print(aggregate_amount(['Fred', 'Ed', 'Peg']))
    print("{0:.2f}".format(average_amount()))
