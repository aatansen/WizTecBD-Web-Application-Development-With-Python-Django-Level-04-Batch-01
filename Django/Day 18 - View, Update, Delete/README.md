# Context

- [Context](#context)
  - [View Page](#view-page)
  - [Delete Data](#delete-data)
  - [Edit \& Update Data](#edit--update-data)

> It is continuation of [Day 16](../Day%2016%20-%20Setup%20Everything%20Inside%20App,%20Data%20Add%20From%20Frontend%20And%20Show/)

## View Page

- In our [student-list.html](./school_app/templates/student-list.html) we will add a new column `action` which will have three `a tag`

  ```jinja
  <table class="table table-striped">
    <thead>
      <tr>
        ...
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      {% for student in student_data %}
        <tr>
          ...
          <td>
            <a href="" class="badge text-bg-success">View</a>
            <a href="" class="badge text-bg-warning">Edit</a>
            <a href="" class="badge text-bg-danger">Delete</a>
          </td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
  ```

- From three of those action first we will work with `View` which needed a link as an action to work
- This link will be for a new page which will be [view-student.html](./school_app/templates/view-student.html)
- Render this inside [views.py](./school_app/views.py)

  ```py
  def view_student(request,id):
    student_data=studentModel.objects.get(id=id)
    context={
      'student_data':student_data,
    }
    return render(request,'view-student.html',context=context)
  ```

- Add URL patterns in [urls.py](./school_app/urls.py)

  ```py
  urlpatterns = [
      ...
      path('view-student/<str:id>/',view_student,name='view_student'),
  ]
  ```

- Now we will use this URL in our action `view` link in [student-list.html](./school_app/templates/student-list.html)

  ```jinja
  <a href="{% url 'view_student' student.id %}" class="badge text-bg-success">View</a>
  ```

- Now in [view-student.html](./school_app/templates/view-student.html) page we will pass the key of dictionary and access the values by the model field name

  ```jinja
  {% extends 'master/base.html' %}

  {% block content %}
  <h1>View student info</h1>

  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">{{student_data.name}}</h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">{{student_data.age}}</h6>
      <h6 class="card-subtitle mb-2 text-body-secondary">{{student_data.roll_no}}</h6>
    </div>
  </div>

  {% endblock content %}
  ```

---
[⬆️ Go to Context](#context)

## Delete Data

- To delete a data from database we will create a function in [views.py](./school_app/views.py)

  ```py
  def delete_student(request,id):
    student_data=studentModel.objects.get(id=id)
    student_data.delete()
    return redirect('student_list')
  ```

- Create URL patter in [urls.py](./school_app/urls.py)

  ```py
  urlpatterns = [
      ...
      path('delete-student/<str:id>/',delete_student,name='delete_student'),
  ]
  ```

- Now link this to `href` of delete action in [student-list.html](./school_app/templates/student-list.html)

---
[⬆️ Go to Context](#context)

## Edit & Update Data

- It is similar to Add data, the extra step is return the data which is already in database so we can edit it
- Create an HTML [edit-student.html](./school_app/templates/edit-student.html) page where we will edit the data

  - We will use same form where we add student data

    ```jinja
    {% extends 'master/base.html' %}

    {% block content %}
      <form method="POST">
        {% csrf_token %}
        <div class="mb-3">
          <label for="" class="form-label">Name</label>
          <input type="text" name="name" value="{{student_data.name}}" class="form-control" required />
        </div>
        <div class="mb-3">
          <label for="" class="form-label">Age</label>
          <input type="number" name="age" value="{{student_data.age}}" class="form-control" required />
        </div>
        <div class="mb-3">
          <label for="" class="form-label">Roll No</label>
          <input type="number" name="roll_no" value="{{student_data.roll_no}}" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    {% endblock %}
    ```

    - Only difference is we added `value` attribute

- Create a function in [views.py](./school_app/views.py) to render that page

  ```py
  def update_student(request,id):
    student_data=studentModel.objects.get(id=id)
    context={
      'student_data':student_data,
    }
    return render(request,'edit-student.html',context=context)
  ```

  - We are sending data of that specific person using get in [edit-student.html](./school_app/templates/edit-student.html) so that we can see the existing data in HTML page using `value` attribute
  - Now we will update this function to accept the modified data to save

    ```py
    def update_student(request,id):
      student_data=studentModel.objects.get(id=id)

      if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        roll_no = request.POST.get('roll_no')

        student_data.name=name
        student_data.age=age
        student_data.roll_no=roll_no
        student_data.save()
        return redirect('student_list')

      context={
        'student_data':student_data,
      }
      return render(request,'edit-student.html',context=context)
    ```

- Add URL pattern in [urls.py](./school_app/urls.py)

  ```py
  urlpatterns = [
      ...
      path('update-student/<str:id>/',update_student,name='update_student'),
  ]
  ```

- Now link this to `href` of edit action in [student-list.html](./school_app/templates/student-list.html)


> [!IMPORTANT]
>
> - When we need single data or specific data we use another parameter in our function which is `id` so that we can get this from our database using `get` query
> - That's why URL pattern also have <str:id>
> - In our case `view`, `delete` and `update` the data from our database we need `id` for that specific data

---
[⬆️ Go to Context](#context)
