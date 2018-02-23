$(document).ready(function () {
    $(".commentbtn").bind('click', function (event) {
        var id = event.target.attributes.nodeValue;
        $(".comentIncoment").toggle(1000);

    });
    console.log(event.target.nodName);

});
