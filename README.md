<h1>Timetable Generation System</h1>
<h3>Project Description</h3> 
<p>The project, Timetable Generation System (SchedAI), is a web application developed using the Django Framework and an SQLite database.</p> 
<p>The project makes use of a genetic algorithm to satisfy the soft and hard constraints and generate the most optimal timetable. The web application includes a simple authentication-authorization module, and on successful authentication, the user is redirected to the admin dashboard.</p> 
<p>On the admin dashboard, the user can input the data of the college/university which is required to generate the timetable. The user must add the following details:</p> 
<ol> 
  <li>Teachers</li> 
  <li>Classrooms</li> 
  <li>Timings</li> 
  <li>Courses</li> 
  <li>Departments</li> 
  <li>Sections</li> 
</ol> 
<p>Upon successful entry of the data into the SQLite database, the user can navigate to the "Generate Timetable" page to start the process of generating the timetable. Upon successful generation of the timetable, the user can download the timetable as a PDF.</p> 
<p>Technologies Used:</p> 
<ul>
  <li>HTML5</li> 
  <li>CSS3</li> 
  <li>Python</li> 
  <li>Django</li> 
  <li>JavaScript</li> 
  <li>sqlite3</li> 
</ul> 


<h3>Troubleshooting Common Issues</h3> 
<h4>Python Error (`runserver`):</h4> 
<p>If you encounter a Python error while running the `runserver` command, follow these steps:</p> 
<ol> 
  <li>Delete the existing virtual environment:</li> 
  <pre><code>rm -r venv</code></pre> 
  <li>Create a new virtual environment:</li> 
  <pre><code>python -m venv venv</code></pre> 
  <li>Activate the virtual environment:</li> 
  <pre><code>venv\Scripts\activate</code></pre> 
</ol> 

<h4>Django Error:</h4> 
<p>If there's an issue with Django, try the following:</p> 
<ol> 
  <li>Navigate up one directory:</li> 
  <pre><code>cd ..</code></pre> 
  <li>Install Django:</li> 
  <pre><code>pip install Django</code></pre> 
</ol> 

<h4>xhtml2pdf Error:</h4> 
<p>If the `xhtml2pdf` library causes issues, use the following steps:</p> 
<ol> 
  <li>Navigate up one directory:</li> 
  <pre><code>cd ..</code></pre> 
  <li>Install or reinstall xhtml2pdf:</li> 
  <pre><code>pip install xhtml2pdf</code></pre> 
  <li>Update `requirements.txt`:</li> 
  <pre><code>pip freeze > requirements.txt</code></pre> 
</ol> 

<h3>How to run the Project?</h3> 
<ol> 
  <li>Clone the Repository</li> 
  <li>Access the project files using an IDE(PyCharm) or text-editor (VS code) or via the command line.</li>
  <li>Navigate to the main project directory:</li> 
  <pre><code>cd .\projttgs\</code></pre> 
  <li>Run the command:</li> 
  <pre><code>python manage.py runserver</code></pre> 
  <li>Open your browser and access localhost at <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a></li> </ol> 
