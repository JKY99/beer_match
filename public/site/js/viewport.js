$(document).ready(function(){
    /*웹페이지 열었을 때*/
    $("#img1").show();
    $("#img2").hide();

    /*img1을 클릭했을 때 img2를 보여줌*/
    $("#img1").click(function(){
        $("#img1").hide();
        $("#img2").show();
    });

    /*img2를 클릭했을 때 img1을 보여줌*/
    $("#img2").click(function(){
        $("#img1").show();
        $("#img2").hide();
    });
});