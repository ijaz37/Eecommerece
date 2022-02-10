$(document).ready(function (){
    var count=0
    $("#s1").click(function (){

        $("#s1").css("color","orange");
        $("#s2").css("color","black");
        $("#s3").css("color","black");
        $("#s4").css("color","black");
        $("#s5").css("color","black");
        count=1;
         $("#total").val(count)
    });
     $("#s2").click(function (){

        $("#s1").css("color","orange");
        $("#s2").css("color","orange");
        $("#s3").css("color","black");
        $("#s4").css("color","black");
        $("#s5").css("color","black");
        count=2;
         $("#total").val(count)
    });
     $("#s3").click(function (){

        $("#s1").css("color","orange");
        $("#s2").css("color","orange");
        $("#s3").css("color","orange");
        $("#s4").css("color","black");
        $("#s5").css("color","black");
        count=3;
         $("#total").val(count)

    });
     $("#s4").click(function (){

        $("#s1").css("color","orange");
        $("#s2").css("color","orange");
        $("#s3").css("color","orange");
        $("#s4").css("color","orange");
        $("#s5").css("color","black");
        count=4;
         $("#total").val(count)
    });
     $("#s5").click(function (){

        $("#s1").css("color","orange");
        $("#s2").css("color","orange");
        $("#s3").css("color","orange");
        $("#s4").css("color","orange");
        $("#s5").css("color","orange");
        count=5;
         $("#total").val(count)
    });

     $("#total").val(count)

});


// $(document).ready(function () {
//     $(".cart-plus").click(function () {
//         debugger;
//         var my_id = 1;
//
//        $.ajax({
//             method: "GET",
//             url: "increment/",
//             data: my_id,
//             success: function (response) {
//                 console.log("abc");
//             }
//         })
//
//     });
// });
//

$(document).ready(function () {
    var common = $("#myprice").val();
    common = parseFloat(common);

    $(".cart-minus").click(function () {
        var my_id = $(this).attr("id").toString();
        var elm = this.parentNode.children[2];
        var total_amount = $("#total_amount").val();

        var sub_total = $("#sub").html();
        var value = $("#qty").val();
        price = $("#myprice").val();
        sub_total = parseFloat(sub_total);
        price = parseFloat(price);
        value = parseFloat(value);
        if (value >= 1) {
            newvalue = value - 1;
            var total = price * newvalue;
            sub_total = sub_total - common;
            total_amount = sub_total;
            var my_id = $(this).attr("id");
            $.ajax({
                method: "GET",
                url: "/decrement/" + my_id,
                data: my_id,
                success: function (response) {
                    console.log("abc");
                    $("#qty").val(newvalue);
                    $("#total").html("$" + total);
                    $("#sub").html(sub_total);
                    $("#total_amu").html("$" + total_amount);
                }

            });
        }

    });

    $(".cart-plus").click(function () {

        var sub_total = $("#sub").html();
        var total_amount = $("#total_amount").val();
        var price = $("#myprice").val();
        var value = $("#qty").val();

        sub_total = parseFloat(sub_total);

        price = parseFloat(price);
        value = parseFloat(value)
        newvalue = value + 1;
        var total = price * newvalue;
        sub_total = sub_total + common;
        total_amount = sub_total;
        var my_id = $(this).attr("id");
        $.ajax({
            method: "GET",
            url: "/increment/"+my_id,
            data: my_id,
            success: function (response) {
                console.log("abc");
                $("#qty").val(newvalue);
                $("#total").html("$" + total);
                $("#sub").html(sub_total);
                $("#total_amu").html("$" + total_amount);
            }
        })

    });


});



