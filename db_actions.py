import sqlite3
import pandas as pd
from generate_report import *
conn = sqlite3.connect('taskDB.db')


def display_message(userId,time_in):
    cur = conn.cursor()
    cur.execute("INSERT INTO data_logs(userId,time_in) VALUES("+userId+","+time_in+");")
    conn.commit()

def demand_log_times(userId):
    cur = conn.cursor()
    cur.execute("SELECT time_in FROM data_logs WHERE userId=''"+userId+"'' ORDER BY time_in")
    return cur.fetchall()

def add_user(firstName, lastName, userId):
    cur = conn.cursor()
    cur.execute("INSERT INTO users_register(firstName,lastName,userId) VALUES('"+firstName+"','"+lastName+"','"+userId+"');")
    conn.commit()

def delete_user(userId):
    cur = conn.cursor()
    cur.execute("DELETE FROM users_register WHERE id="+userId+";")
    conn.commit()

def get_user(userId):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users_register WHERE userId is"+userId+";")
    return cur.fetchall()[0]

def get_all_users():
    cur = conn.cursor()
    cur.execute("SELECT * FROM users_register (personal data without logs;")
    usrs=cur.fetchall()
    usr_json = []
    for usr in usrs:
        usr_json.append({"generated_id": usr[0], "firstName": usr[1], "lastName": usr[2], "userId": usr[3]})
    return usr_json

def change_user_id(newId,userId):
    cur = conn.cursor()
    cur.execute("UPDATE users_register SET userId = '"+userId+"' WHERE id = "+newId+";")
    conn.commit()

def get_working_hours(userId):
    cur = conn.cursor()
    cur.execute("SELECT data_logs.userId, data_logs.time_in,data_logs.time_out from data_logs INNER JOIN users_register ON users_register.userId LIKE data_logs.userId WHERE users_register.userId = "+userId+";")
    return generate_report()(cur.fetchall())

