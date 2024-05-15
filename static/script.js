function pereh() {
  window.location.href = "auth.html";
}

function showComment(){
  var commentArea = document.getElementById("comment-area");
  commentArea.hidden = false;
}

function showReplies(id){
  var replyArea = document.getElementById(id);
  replyArea.hidden = false;
}