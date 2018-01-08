# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 11:30:37 2017

@author: kmcgi
"""

import mysql.connector
import csv

totalNumList = []
numPassList = []
numCloneList = []
numPass = []
numPassDict = {}
constructPassList = []
numConstructPassList = []
numCloneDict = {}
numConstructDict = {}


def get_db_connection():
    """Return a connection to the database using mysql.connector."""
    conn = mysql.connector.connect(
        user="cam",
        password="monsanto",
        host="camprod.monsanto.com",
        database="nextgen")
    return conn



def get_num_construct_pass_for_Round(conn, geRound):
    sql1 = """
        select 
            tbl_seq_results.observed_design_id, tbl_seq_results.pass_fail, tbl_construct_alias.Construct_Name
        from
            tbl_seq_results
        join
            tbl_design on tbl_seq_results.observed_design_id = tbl_design.design_id
        join
            tbl_construct_alias on tbl_design.product_construct_id = tbl_construct_alias.Construct_ID
        where 
            tbl_seq_results.processing_round = %s
    """ % (geRound)
    
    cursor = conn.cursor(dictionary = True)
    cursor.execute(sql1)
    samples = cursor.fetchall()
    cursor.close()
    
    return samples
    
    
    
    
def get_pass_fail_for_Round(conn, geRound):
    """Return a list of pass/fail statuses for all clones sequenced in a GE Round"""
    sql1 = """
        select
            tbl_seq_results.pass_fail
        from
            tbl_seq_results
        inner join
            tbl_clone_tracking
        on 
            tbl_seq_results.clone_id=tbl_clone_tracking.clone_id
        where
            tbl_clone_tracking.processing_round = %s
        
    """ % (geRound)
    cursor = conn.cursor(dictionary = True)
    cursor.execute(sql1)
    samples = cursor.fetchall()
    cursor.close()
    
    return samples


def get_num_seq_reads_for_Round(conn, geRound):
    sql1 = """
        select 
            tbl_seq_results.read_count
        from
            tbl_seq_results
        where
            tbl_seq_results.processing_round = %s
    """ % (geRound)
    
    cursor = conn.cursor(dictionary = True)
    cursor.execute(sql1)
    samples = cursor.fetchall()
    cursor.close()
    
    return samples  


x = 0
geRounds = []
rowList = []
with open("P:\\Production\\GE Team\\TeamMtg\\testNewExperimentTracker.csv", 'rb') as openfile:
    reader = csv.reader(openfile)
    for row in reader:
        if x < 7:
            rowList.append(row)
            x += 1

        else:
            if row[2] == '':
                continue
            else:
                geRounds.append(row[2])
                rowList.append(row)

    
for i in geRounds:
    totalNumDict = {}
    constructPassList = []
    numPass = []
    numPassDict = {}
    numConstructDict = {}
    totalNum = 0
    pass_fail = get_pass_fail_for_Round(get_db_connection(), i)
    constructs = get_num_construct_pass_for_Round(get_db_connection(), i)
    
    for construct in constructs:
        for k, v in construct.items():
            if construct['pass_fail'] == "pass":
                constructPassList.append(construct['observed_design_id'])

    constructList = list(set(constructPassList))
    numConstructs = len(constructList)

    numClones = len(pass_fail)
   
    for sample in pass_fail:
        for k, v in sample.items():
            if v == 'pass':
                numPass.append(v)
                
                
    numSeqReads = get_num_seq_reads_for_Round(get_db_connection(), i)
    
    
    for read in numSeqReads:
        for k, v in read.items():
            if v == None:
                continue
            else:
                totalNum += int(v)
            
                
    totalNumDict[i] = totalNum
    totalNumList.append(totalNumDict)            
    numConstructDict[i] = numConstructs
    numConstructPassList.append(numConstructDict)
    numPassDict[i] = len(numPass)
    numPassList.append(numPassDict)
    numCloneDict[i] = numClones
    numCloneList.append(numCloneDict)



rowList2 = []   
w = 0
#with open("C:/Users/kmcgi/Documents/Python Scripts/Experiment Tracker.csv", 'wb') as outputfile:
with open("P:\\Production\\GE Team\\TeamMtg\\testNewExperimentTrackerUpdated.csv", 'wb') as outputfile:
    writer = csv.writer(outputfile)
    

            
    for i in numPassList:
        for x in numCloneList:
            for c in numConstructPassList:
                for n in totalNumList:

                    for k, v in i.items():
                        for key, value in x.items():
                            for g, m in c.items():
                                for a, b in n.items():
                                    if key == k:
                                        if key == g:
                                            if key == a:
                                                row = [k, m, value, v, b]
        rowList2.append(row)

    for i in rowList2:                           
        for rows in rowList:

            if w < 7:
                writer.writerow(rows)
                w += 1
            else:
                if rows[2] == i[0]:
                    rows[10] = i[1]
                    rows[11] = i[2]
                    rows[12] = i[3]
                    rows[14] = i[4]
                    writer.writerow(rows)

            
                    
            
                
        

            
    
#print get_num_construct_pass_for_Round(get_db_connection(), 1355)