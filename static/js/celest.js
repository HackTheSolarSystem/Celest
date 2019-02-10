function setSpaceThang(thang) {
  $("#space_thang")[0].innerHTML = thang;

  $("#space_thang_dropdown")[0].classList = "dropdown";

  return false;
}

function setResolution(resolution) {
  $("#resolution")[0].innerHTML = resolution;

  $("#resolution_dropdown")[0].classList = "dropdown";

  return false;
}

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

function startDownload () {

/*  $.ajax({
    url: url,
    data: data,
    success: success,
    dataType: "json"
  });
*/

  var start_date, start_time, end_date, end_time, source_id, start_date = "";



    var progressbar = $( "#progressbar" ), progressLabel = $( ".progress-label" );
 
    progressbar.progressbar({
      value: false,
      change: function() {
        progressLabel.text( progressbar.progressbar( "value" ) + "%" );
      },
      complete: function() {
        progressLabel.text( "Download Complete!" );
      }
    });
 
    function progress() {
      var val = progressbar.progressbar( "value" ) || 0;
 
      progressbar.progressbar( "value", val + 2 );
 
      if ( val < 99 ) {
        setTimeout( progress, 80 );
      }
    }
 
    setTimeout( progress, 2000 );
}

$(document).ready(
  function(){
    for (current_col = 0; current_col < source_list[0].values.length; current_col++) {
      var source_name = source_list[0].values[current_col].name;

      var div_head = $("#data_source_col_" + current_col);
      var body = $("<div class='collapse' id='data_source_col_body_" + current_col + "'></div>");
      var header = $("<h3><input type='checkbox' id=" + source_name + "'>" + source_name + "</input></h3>");
      var collapse_button = $("<span class='collapse-button'><button data-toggle='collapse' data-target='#data_source_col_body_" + current_col + "'>+</button></span>");

      header.append(collapse_button);

      div_head.append(header);
      div_head.append(body);

      makeList(source_list[0].values[current_col].values, $("#data_source_col_body_" + current_col));
    }

    $("#download").click(function(){
      startDownload();

      var query_string = "[{" + start_date + "}]"; // JSON data to send to Python script
    });

    $("#resolution_list").children().click(function(){
      setResolution(this.innerText);

      return false;
    });

    $("#space_thang_sun").click(function(){
      setSpaceThang(this.innerText);

      return false;
    });
});
