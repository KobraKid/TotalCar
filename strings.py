header = """
<html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    </head>
    </body>
        <div class="container">
            <div class="row">
"""

footer = """
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    </body>
</html>
"""

card = """
<div class="card" style="width: 18rem;">
    <img src="https://amp.businessinsider.com/images/5b97c8db5c5e5223008b606a-1334-1001.jpg" class="card-img-top" alt="%s %s">
    <div class="card-body">
        <h5 class="card-title">%s %s (%s)</h5>
        <i class="card-text" style="color: gray">%s miles</i>
    </div>
    <ul class="list-group list-group-flush">
        <li class="list-group-item">Last fill-up: %s miles ago</li>
        <li class="list-group-item">Last oil change: %s miles ago</li>
        <li class="list-group-item">Last tire rotation: %s miles ago</li>
    </ul>
    <div class="card-body">
        <a href="#" class="btn btn-primary" data-toggle="modal" data-target="%s">Details</a>
    </div>
</div>
"""

details_modal = """
<div class="modal fade" id="%s" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
"""
