from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_view(request):
    return HttpResponse(''' 
        <h1>Welcome to our Website</h1>
                        
''')

# Python code + HTML Code =====> Not Recommended to mix python code with html code.
def home_view(request):
    return HttpResponse("""
        <h1>Home Page</h1>
        <p>Welcome to our website!</p>           
""")

def about_view(request):
    return HttpResponse("""
        <h1>About Page</h1>
        <p>Welcome to our website!</p>           
""")


def course_view(request):
    return HttpResponse("""
        <h1>Course Page</h1>
        <p>Welcome to our website!</p> 
        <ul>
            <li>Python Course</li>
            <li>Django Course</li>
            <li>Java Course</li>
        </ul>          
""")

def contact_view(request):
    return HttpResponse("""
        <h1>Contact Page</h1>
        <p>Welcome to our website!</p>    
               
""")
