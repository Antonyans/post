
$('#search-form').bind('keyup submit',function(e) {
      $.get("search/", $(this).serialize(), function(data) {
        $('.posts').html(data);
        console.log(data);
        if (data){
          $('.divforpostsWiew').hide();
          $('.postAddClass').hide();

        }


    });
    e.preventDefault();

});
