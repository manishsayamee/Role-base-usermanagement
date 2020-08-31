<!-- 
{% extends 'accounts/base.html' %}
{% block content %}
<style>
  .container{
  background-color:#7a3f79;
}
.sign{
  margin-top: 20px;margin-left: 25%;color:white; 
}
.card{

  padding: 30px; border-radius: 10px; width:50%; margin:auto
}
.btn{
  background-color: #4373d9;
  width:20%
}
</style>

<body class="container">
  <h1  class="sign" style="font-family:Times New Roman;">Upload File</h1>
  <div class="card">
      <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
          <div class="form-group">
              <label>Title</label>
              <input type="text" class="form-control" placeholder="Title" name="title" required>
          </div>
          <div class="form-group">
            <label>File</label>
            <input type="file" class="form-control" placeholder="Upload File" name="file" required>
          </div>
          <select name="Type" >
            <option value='Image'>Image</option>
            <option value = 'pdf'>pdf</option>
            <option value = 'Video'>Video</option>
          </select>


          <button type="submit" class="btn btn-primary">Submit</button>
      </form>
  </div>
  
  </body>
  {% endblock %}  -->
