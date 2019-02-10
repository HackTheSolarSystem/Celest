var url = 'pulldata.py';

var current_col = 0;

function makeList(array, root){
  if(typeof array[0].node !== 'undefined'){
    if(array[0].node == 'parent') {
      makeList(array[0].values, root);
      return;
    }
  }

  var ul = $("<ul style='list-style-type:none; padding-left: 0px;'></ul>");

  root.append(ul);

  for (var i = 0; i < array.length; i++) {
    var li = $("<li style='padding-left: 5px'></li>");
    ul.append(li);
    var check_box = $("<input type='checkbox' id=" + array[i].value + "'>" + array[i].name + "</input>");
    li.append(check_box);

    if(typeof array[i].values !== 'undefined'){
      makeList(array[i].values, li);
    }
  }
}

$(document).ready(
  function(){
    for (current_col = 0; current_col < source_list[0].values.length; current_col++) {
      var ul = $("<ul style='list-style-type:none; padding-left: 0px;'></ul>");
      var li = $("<li style='padding-left: 5px'></li>");
      ul.append(li);
      var check_box = $("<input type='checkbox' id=" + source_list[0].values[current_col].value + "'>" + source_list[0].values[current_col].name + "</input>");
      li.append(check_box);
      $("#data_source_col_" + current_col).append(ul);
      makeList(source_list[0].values[current_col].values, li);
    }

    $("#download").click(function( event ) {
      var start_date = $("#start_date").val();
      var start_time = $("#start_time").val();
      var end_date   = $("#end_date").val();
      var end_time   = $("#end_time").val();
      var source_id  = $("#source_id").val();
      var start_date = $("#start_date").val();

      var query_string = "[{" + start_date + "}]"; // JSON data to send to Python script
    });

/*  $.ajax({
    url: url,
    data: data,
    success: success,
    dataType: "json"
  });
*/
});
