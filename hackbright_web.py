"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    grades_titles = hackbright.get_grades_by_github(github)

    html = render_template('student_info.html', first=first,
                           last=last,
                           github=github,
                           grades_titles=grades_titles)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route('/student-creation')
def display_student_add():
    """displays student add"""

    return render_template('student_add.html')


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

# Is there a way to capture different values all at one time instead of 
#separately as below? No.

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    return render_template('add_confirmation.html', github=github)


# @app.route('/project-selection')
# def display_project_selection():
#     """"display project title selection page"""

#     return render_template('select_project.html')

@app.route('/project')
def display_project():
    """display project"""

    project_title = request.args.get('project')
    title, description, max_grade = hackbright.get_project_by_title(project_title)

    return render_template('project_info.html', title=title,
                           description=description,
                           max_grade=max_grade)




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
