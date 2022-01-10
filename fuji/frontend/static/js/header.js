$(function(){
    $(document).click( function(e){
        if ( $(e.target).closest('#sign__avatar').length ) {
            $('#sign__setting').show()
            return
        }
        else if ( $(e.target).closest('#sign__setting').length ) {
            return
        }
    
        $('#sign__setting').hide();
    })
})