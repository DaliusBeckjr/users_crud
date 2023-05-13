from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user

@app.route('/')
def root():
    return redirect("/users/dashboard")

@app.route('/users/dashboard')
def users_dashboard():
    # import user - to call method you need to use lowercase
    # before entering the class
    # equal to a var that is doing a method call to our get_all user(cls)
    # method
    users = user.User.get_all_users()
    # or users = User.get_all_users() for from user import User
    print(" ")
    print(users)
    print(" ")
    return render_template('users_dashboard.html', all_users=users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    user.User.save_user(data)
    return redirect('/users/dashboard')

# route that takes us to the get one user dashboard
@app.route('/users/show/<int:id>')
def show_user(id):
    data={
        'id': id 
    }
    return render_template('show_user.html', one_user= user.User.get_one_user(data))

#crud method edit/ update route
# for the post method, build it out as /users/update
@app.route('/users/edit/<int:id>')
def edit_user(id):
    data={
        'id': id
    }
    return render_template('edit_user.html', one_user= user.User.get_one_user(data))

# update route
@app.route('/users/update', methods=['POST'])
def update_user():
    # we dont need to store the method call in any var 
    user.User.update_user(request.form)
    return redirect(f"/users/show/{request.form['id']}")

# delete route
@app.route('/users/delete/<int:id>')
def delete_user(id):
    data={
        'id': id 
    }
    user.User.delete_user(data)
    return redirect('/users/dashboard')