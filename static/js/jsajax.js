  $(document).ready(function(){

    		$(document).on('keydown', '#id_username',function(){
          $('#imgLoad').show();
          $('#imgTrue').hide();
          $('#imgFalse').hide();
    			setTimeout(check, 2000);

function check(){
$.ajax({
  type: "GET",
  url:"/chek_username",
  data:{
    "username": $('#id_username').val(),
  },
  dataType: "text",
  cache: false,

  success: function(data){
    if (data == 'ok'){
      $('#imgLoad').hide();
      $('#imgTrue').show();
      $('#imgFalse').hide();

    }
    else if(data == 'no'){
      $('#imgLoad').hide();
      $('#imgTrue').hide();
      $('#imgFalse').show();

    }
  }
});
};
});
///////////////////////////////////////////////check_email////////////////////////////
$(document).on('keydown', '#id_email', function(){
  $('#imgLoadEmail').show();
  $('#imgTrueEmail').hide();
  $('#imgFalseEmail').hide();
  setTimeout(check_email, 2000);

  function check_email(){
    $.ajax({
      type: "GET",
      url: "/check_email",
      data: {
        "email": $('#id_email').val(),
      },
      dataType: "text",
      cache: false,

      success: function(data){
        if (data == 'ok'){
          console.log('ok')
          $('#imgLoadEmail').hide();
          $('#imgTrueEmail').show();
          $('#imgFalseEmail').hide();
          $('#emailEror').hide();
        }
        else if(data == 'no'){
          console.log('no')

          $('#imgLoadEmail').hide();
          $('#imgTrueEmail').hide();
          $('#imgFalseEmail').show();
          $('#emailEror').show();

        }
      }
    });
  };
});
///////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////Check_password///////////////////////////
$(document).on( 'keydown', '#id_password2',function(){
  $('#imgLoadPass').css('display', 'block');
  $('#imgTruePass').hide();
  $('#imgFalsePass').hide();
  setTimeout(check_password, 2000);
});

  function check_password(){
    var pass1 = $('#id_password1').val();
    var pass2 = $('#id_password2').val();

    if(pass1 == pass2){
      $('#imgTruePass').show();
      $('#imgLoadPass').hide();
      $('#imgFalsePass').hide();
      $('#passError').hide();
      $('#pass2-helptext').show();
    }
    else {
      $('#imgTruePass').hide();
      $('#imgLoadPass').hide();
      $('#imgFalsePass').show();
      $('#pass2-helptext').hide();
      $('#passError').show();
    }
  };
//////////////////////////////////////////////////////////
});
