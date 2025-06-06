from django.shortcuts import render

def student_view(request):

    students = [
        {'name':'Amit', 'roll':101, 'course':'Full Stack'},
        {'name':'Doreamon', 'roll':102 , 'course':'MERN Stack'},
        {'name':'Nobita', 'roll':103, 'course':'Java Full Stack'},
        {'name':'Raju', 'roll':104, 'course':'.Net Full Stack'},

    ]

    dict={'students':students}

    return render(request,'testapp/student.html',dict)
