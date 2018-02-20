// $(document).ready(function(){
//     $(document).on('click', '#searchPost', function(){
//       function searchPost(){
//         $.ajax({
//           type: "GET",
//           url: "/search/",
//           data: {
//             "q": $('#searchPost').val()
//           },
//           dataType: "text",
//           cache: false,
//
//           success: function(data){
//             if (data == 'ok'){
//               alert('aaa');
//             }
//             else if(data == 'no'){
//               alert('aaa');
//
//             }
//           }
//         });
//       }
//     });
// });

// $('#search-form').submit(function(e){
//     $.get'search/', $(this).serialize(), function(data){
//       $('#posts').html(data);
//     });
//     e.preventDefault();
// });



$('#search-form').submit(function(e) {
  // var txt = $("#search-form").val();

    $.get("search/", $(this).serialize(), function(data) {
        $('#posts').html(data);
        console.log(data);
    });
    e.preventDefault();
});
