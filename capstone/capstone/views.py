from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render



def LogsListView(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT seq, event, create_date, hash, message FROM log"
        result = cursor.execute(strSql)
        logs = cursor.fetchall()

        connection.commit()
        connection.close()

    except:
        connection.rollback()
        print("Failed selecting in LogsListView")

    #return HttpResponse(logs) 
    return render(request, 'logs_list.html', {'logs': logs})