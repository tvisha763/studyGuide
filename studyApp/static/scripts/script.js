$(document).ready(function(){

    $('.sale').hide()
    $('.practice').hide()
    $('.tutoring').hide()
    $('.postType').change(function(){
        let val = $('.postType').val()
        if (val == 1) {
            $('.sale').show()
            $('.practice').hide()
            $('.tutoring').hide()
        } else if(val == 2) {
            $('.sale').hide()
            $('.practice').show()
            $('.tutoring').hide()
        } else if(val == 3) {
            $('.sale').hide()
            $('.practice').hide()
            $('.tutoring').show()
        } else {
            $('.sale').hide()
            $('.practice').hide()
            $('.tutoring').hide()
        }
        
        
    });

    
});